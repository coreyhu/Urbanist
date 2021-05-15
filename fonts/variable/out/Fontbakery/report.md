## Fontbakery report

Fontbakery version: 0.7.35

<details>
<summary><b>[1] Family checks</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Is the command `ftxvalidator` (Apple Font Tool Suite) available?</summary>

* [com.google.fonts/check/ftxvalidator_is_available](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/ftxvalidator_is_available)
<pre>--- Rationale ---
There&#x27;s no reasonable (and legal) way to run the command `ftxvalidator` of the
Apple Font Tool Suite on a non-macOS machine. I.e. on GNU+Linux or Windows etc.
If Font Bakery is not running on an OSX machine, the machine running Font Bakery
could access `ftxvalidator` on OSX, e.g. via ssh or a remote procedure call
(rpc).
There&#x27;s an ssh example implementation at:
https://github.com/googlefonts/fontbakery/blob/main/prebuilt/workarounds
/ftxvalidator/ssh-implementation/ftxvalidator</pre>

* ⚠ **WARN** Could not find ftxvalidator. [code: ftxvalidator-available]

</details>
<br>
</details>
<details>
<summary><b>[12] UrbanistGX.ttf</b></summary>
<details>
<summary>💔 <b>ERROR:</b> Familyname must be unique according to namecheck.fontdata.com</summary>

* [com.google.fonts/check/fontdata_namecheck](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/fontdata_namecheck)
<pre>--- Rationale ---
We need to check names are not already used, and today the best place to check
that is http://namecheck.fontdata.com</pre>

* 💔 **ERROR** Failed to access: http://namecheck.fontdata.com.
		This check relies on the external service http://namecheck.fontdata.com via the internet. While the service cannot be reached or does not respond this check is broken.

		You can exclude this check with the command line option:
		-x com.google.fonts/check/fontdata_namecheck

		Or you can wait until the service is available again.
		If the problem persists please report this issue at: https://github.com/googlefonts/fontbakery/issues

		Original error message:
		<class 'requests.exceptions.ReadTimeout'> [code: namecheck-service]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking file is named canonically.</summary>

* [com.google.fonts/check/canonical_filename](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename)
<pre>--- Rationale ---
A font&#x27;s filename must be composed in the following manner:
&lt;familyname&gt;-&lt;stylename&gt;.ttf
- Nunito-Regular.ttf,
- Oswald-BoldItalic.ttf
Variable fonts must list the axis tags in alphabetical order in square brackets
and separated by commas:
- Roboto[wdth,wght].ttf
- Familyname-Italic[wght].ttf</pre>

* 🔥 **FAIL** The file 'UrbanistGX.ttf' must be renamed to 'Urbanist[ital,wght].ttf' according to the Google Fonts naming policy for variable fonts. [code: bad-varfont-filename]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Checking OS/2 usWeightClass.</summary>

* [com.google.fonts/check/usweightclass](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/usweightclass)
<pre>--- Rationale ---
Google Fonts expects variable fonts, static ttfs and static otfs to have
differing OS/2 usWeightClass values.
For Variable Fonts, Thin-Black must be 100-900
For static ttfs, Thin-Black can be 100-900 or 250-900
For static otfs, Thin-Black must be 250-900
If static otfs are set lower than 250, text may appear blurry in legacy Windows
applications.
Glyphsapp users can change the usWeightClass value of an instance by adding a
&#x27;weightClass&#x27; customParameter.</pre>

* 🔥 **FAIL** OS/2 usWeightClass is '400' when it should be '900'. [code: bad-value]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: FONT_SUBFAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/subfamilyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/subfamilyname)

* 🔥 **FAIL** SUBFAMILY_NAME for Mac "Regular" must be "Black" [code: bad-familyname]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check name table: TYPOGRAPHIC_SUBFAMILY_NAME entries.</summary>

* [com.google.fonts/check/name/typographicsubfamilyname](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/typographicsubfamilyname)
<pre>--- Rationale ---
Requirements for the TYPOGRAPHIC_SUBFAMILY_NAME entries in the &#x27;name&#x27; table.</pre>

* 🔥 **FAIL** TYPOGRAPHIC_SUBFAMILY_NAME for Win "Regular" is incorrect. It must be "Black". [code: bad-typo-win]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Check that variable fonts have an HVAR table.</summary>

* [com.google.fonts/check/varfont/has_HVAR](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont/has_HVAR)
<pre>--- Rationale ---
Not having a HVAR table can lead to costly text-layout operations on some
platforms, which we want to avoid.
So, all variable fonts on the Google Fonts collection should have an HVAR with
valid values.
More info on the HVAR table can be found at:
https://docs.microsoft.com/en-us/typography/opentype/spec
/otvaroverview#variation-data-tables-and-miscellaneous-requirements</pre>

* 🔥 **FAIL** All variable fonts on the Google Fonts collection must have a properly set HVAR table in order to avoid costly text-layout operations on certain platforms. [code: lacks-HVAR]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Font enables smart dropout control in "prep" table instructions?</summary>

* [com.google.fonts/check/smart_dropout](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/smart_dropout)
<pre>--- Rationale ---
This setup is meant to ensure consistent rendering quality for fonts across all
devices (with different rendering/hinting capabilities).
Below is the snippet of instructions we expect to see in the fonts:
B8 01 FF    PUSHW 0x01FF
85          SCANCTRL (unconditinally turn on
                      dropout control mode)
B0 04       PUSHB 0x04
8D          SCANTYPE (enable smart dropout control)
&quot;Smart dropout control&quot; means activating rules 1, 2 and 5:
Rule 1: If a pixel&#x27;s center falls within the glyph outline,
        that pixel is turned on.
Rule 2: If a contour falls exactly on a pixel&#x27;s center,
        that pixel is turned on.
Rule 5: If a scan line between two adjacent pixel centers
        (either vertical or horizontal) is intersected
        by both an on-Transition contour and an off-Transition
        contour and neither of the pixels was already turned on
        by rules 1 and 2, turn on the pixel which is closer to
        the midpoint between the on-Transition contour and
        off-Transition contour. This is &quot;Smart&quot; dropout control.
For more detailed info (such as other rules not enabled in this snippet), please
refer to the TrueType Instruction Set documentation.</pre>

* 🔥 **FAIL** The 'prep' table does not contain TrueType instructions enabling smart dropout control. To fix, export the font with autohinting enabled, or run ttfautohint on the font, or run the `gftools fix-nonhinting` script. [code: lacks-smart-dropout]

</details>
<details>
<summary>🔥 <b>FAIL:</b> Ensure VFs do not contain slnt or ital axes. </summary>

* [com.google.fonts/check/varfont/unsupported_axes](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/varfont/unsupported_axes)
<pre>--- Rationale ---
The &#x27;ital&#x27; and &#x27;slnt&#x27; axes are not supported yet in Google Chrome.
For the time being, we need to ensure that VFs do not contain either of these
axes. Once browser support is better, we can deprecate this check.
For more info regarding browser support, see:
https://arrowtype.github.io/vf-slnt-test/</pre>

* 🔥 **FAIL** The "ital" axis is not yet well supported on Google Chrome. [code: unsupported-ital]

</details>
<details>
<summary>⚠ <b>WARN:</b> License URL matches License text on name table?</summary>

* [com.google.fonts/check/name/license_url](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url)
<pre>--- Rationale ---
A known license URL must be provided in the NameID 14 (LICENSE INFO URL) entry
of the name table.
The source of truth for this check is the licensing text found on the NameID 13
entry (LICENSE DESCRIPTION).
The string snippets used for detecting licensing terms are:
- &quot;This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is available with a FAQ at: https://scripts.sil.org/OFL&quot;
- &quot;Licensed under the Apache License, Version 2.0&quot;
- &quot;Licensed under the Ubuntu Font Licence 1.0.&quot;
Currently accepted licenses are Apache or Open Font License.
For a small set of legacy families the Ubuntu Font License may be acceptable as
well.
When in doubt, please choose OFL for new font projects.</pre>

* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]

</details>
<details>
<summary>⚠ <b>WARN:</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering?</summary>

* [com.google.fonts/check/gasp](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/gasp)
<pre>--- Rationale ---
Traditionally version 0 &#x27;gasp&#x27; tables were set so that font sizes below 8 ppem
had no grid fitting but did have antialiasing. From 9-16 ppem, just grid
fitting. And fonts above 17ppem had both antialiasing and grid fitting toggled
on. The use of accelerated graphics cards and higher resolution screens make
this approach obsolete. Microsoft&#x27;s DirectWrite pushed this even further with
much improved rendering built into the OS and apps.
In this scenario it makes sense to simply toggle all 4 flags ON for all font
sizes.</pre>

* ⚠ **WARN** The 'gasp' table does not have an entry that applies for all font sizes. The gaspRange value for such entry should be set to 0xFFFF. [code: lacks-ffff-range]

</details>
<details>
<summary>⚠ <b>WARN:</b> Checking with ots-sanitize.</summary>

* [com.google.fonts/check/ots](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/ots)

* ⚠ **WARN** ots-sanitize passed this file, however warnings were printed:

ERROR: gasp: numRanges is zero
ERROR: Table discarded
 [code: ots-sanitize-warn]

</details>
<details>
<summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points?</summary>

* [com.google.fonts/check/outline_alignment_miss](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss)
<pre>--- Rationale ---
This check heuristically looks for on-curve points which are close to, but do
not sit on, significant boundary coordinates. For example, a point which has a
Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the
baseline, here we also check for points near the x-height (but only for lower
case Latin letters), cap-height, ascender and descender Y coordinates.
Not all such misaligned curve points are a mistake, and sometimes the design may
call for points in locations near the boundaries. As this check is liable to
generate significant numbers of false positives, it will pass if there are more
than 100 reported misalignments.</pre>

* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:
	* Ccedilla: X=970.0,Y=-2.0 (should be at baseline 0?)
	* J: X=181.0,Y=2.0 (should be at baseline 0?)
	* X: X=64.0,Y=1402.0 (should be at cap-height 1400?)
	* X: X=434.0,Y=1402.0 (should be at cap-height 1400?)
	* X: X=1082.0,Y=1402.0 (should be at cap-height 1400?)
	* X: X=1452.0,Y=1402.0 (should be at cap-height 1400?)
	* m: X=491.0,Y=998.5 (should be at x-height 1000?)
	* oslash: X=408.0,Y=-2.0 (should be at baseline 0?)
	* r: X=120.0,Y=998.0 (should be at x-height 1000?)
	* r: X=420.0,Y=998.0 (should be at x-height 1000?) and 21 more. [code: found-misalignments]

</details>
<br>
</details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 1 | 7 | 5 | 97 | 8 | 86 | 0 |
| 0% | 3% | 2% | 48% | 4% | 42% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
