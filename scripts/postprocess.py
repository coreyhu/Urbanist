import re
import os
import glob
import shutil
from fontTools import ttLib
from fontTools.varLib import instancer
from fontTools.ttLib import TTFont
from fontTools.ttLib.ttFont import newTable
from fontbakery.constants import MacStyle, FsSelection, NameID, PlatformID, WindowsEncodingID, WindowsLanguageID, MacintoshEncodingID, MacintoshLanguageID

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

def fix_postscript_names(ttFont, ps_nameids, prefix):

  ttFont['name'].setName(
    prefix, 
    25,
    PlatformID.WINDOWS,
    WindowsEncodingID.UNICODE_BMP,
    WindowsLanguageID.ENGLISH_USA
  )

  ttFont['name'].setName(
    prefix, 
    25,
    PlatformID.MACINTOSH,
    MacintoshEncodingID.ROMAN,
    MacintoshLanguageID.ENGLISH
  )

  for nameid in ps_nameids:
    cur_name = ttFont['name'].getName( 
      nameid,
      PlatformID.WINDOWS,
      WindowsEncodingID.UNICODE_BMP,
      WindowsLanguageID.ENGLISH_USA
    )
    suffix = str(cur_name).split("-")[-1]
    if suffix.endswith("Italic"):
      suffix = suffix[:-6]
    
    if suffix == "":
      suffix = "Regular"

    new_name = "{}-{}".format(prefix, suffix)
    print("Renaming instance {} to {}".format(str(cur_name), new_name))

    ttFont['name'].setName(
      new_name, 
      nameid,
      PlatformID.WINDOWS,
      WindowsEncodingID.UNICODE_BMP,
      WindowsLanguageID.ENGLISH_USA
    )

    ttFont['name'].setName(
      new_name, 
      nameid,
      PlatformID.MACINTOSH,
      MacintoshEncodingID.ROMAN,
      MacintoshLanguageID.ENGLISH
    )    


if __name__ == "__main__":

  roman_path = "../fonts/variable/Urbanist[wght].ttf"
  with open(roman_path, "rb") as f:
    # Fix roman postscript names
    ttFont = TTFont(f)
    ps_nameids = [instance.postscriptNameID for instance in ttFont['fvar'].instances]
    fix_postscript_names(ttFont, ps_nameids, "UrbanistRoman")
    
    # Fix OS/2.fsSelection bit 7
    
    
    ttFont.save(roman_path)


  
  italic_path = "../fonts/variable/Urbanist-Italic[wght].ttf"
  with open(italic_path, "rb") as f:
    # Fix italic postscript names
    ttFont = TTFont(f)
    ps_nameids = [instance.postscriptNameID for instance in ttFont['fvar'].instances]
    fix_postscript_names(ttFont, ps_nameids, "UrbanistItalic")

    # Fix OS/2.fsSelection bit 7

    ttFont.save(italic_path)


  for font_path in glob.glob("../fonts/variable/Urbanist-Italic*.ttf"):
    # set windows subfamily name to Italic in name table
    # For Urbanist-Italic, set ttFont["head"].macStyle = MacStyle.ITALIC
    # Change OS/2.fsSelection to 0x0081 
    with open(font_path, "rb") as f:
      print("Fix italic naming in {}".format(font_path))
      ttFont = TTFont(f)
      ttFont["head"].macStyle = MacStyle.ITALIC
      ttFont['OS/2'].fsSelection = FsSelection.USETYPOMETRICS | FsSelection.ITALIC
      ttFont.save(font_path)
