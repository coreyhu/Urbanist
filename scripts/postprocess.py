import glob
from fontTools import ttLib
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables import _a_v_a_r, _p_o_s_t
from fontTools.ttLib.ttFont import newTable

def fix_italic_angle(ttFont, angle=-8.0):
  post = ttLib.getTableClass("post")()
  post.decompile(ttFont.getTableData("post"), ttFont)
  post.italicAngle = angle
  ttFont['post'] = post

def add_avar_table(ttFont):
  avar = newTable("avar")
  avar.segments = {
    "wght": {
      -1.0: -1.0,
      0: 0,
      1.0: 1.0
    },
    "ital": {
      -1.0: -1.0,
      0: 0,
      1.0: 1.0
    }
  }
  ttFont['avar'] = avar

if __name__ == "__main__":
  with open("../fonts/variable/Urbanist[ital,wght].ttf", "rb") as f:
    ttFont = TTFont(f)
    
  add_avar_table(ttFont)
  ttFont.save("../fonts/variable/Urbanist[ital,wght].ttf")

  for font_path in glob.glob("../fonts/ttf/*Italic.ttf"):
    with open(font_path, "rb") as f:
      ttFont = TTFont(f)
      fix_italic_angle(ttFont)
      ttFont.save(font_path)