#!/usr/bin/env bash

PKG="python3-indico-fonts"

echo "Checking fonts provided by: $PKG"
echo "------------------------------------------------------------"

# Get list of font files from the package
fonts=$(rpm -ql "$PKG" | grep -Ei '\.(ttf|otf|ttc)$')

if [[ -z "$fonts" ]]; then
    echo "No font files found in package $PKG"
    exit 1
fi

# Map: font name → list of installed packages
declare -A installed_fonts

echo "Indexing fonts from all installed packages..."
for pkg in $(rpm -qa | grep fonts | grep -v indico); do
    files=$(rpm -ql "$pkg" 2>/dev/null | grep -Ei '\.(ttf|otf|ttc)$')
    if [[ -n "$files" ]]; then
        for f in $files; do
            # Extract internal font family names (may be comma-separated)
            families=$(fc-scan --format "%{family}\n" "$f" 2>/dev/null)

            # Split on commas
            IFS=',' read -ra names <<< "$families"

            for name in "${names[@]}"; do
                clean=$(echo "$name" | sed 's/^ *//;s/ *$//')
                if [[ -n "$clean" ]]; then
                    installed_fonts["$clean"]+="$pkg "
                fi
            done
        done
    fi
done

echo
echo "Comparing fonts from $PKG with installed packages..."
echo "------------------------------------------------------------"

for f in $fonts; do
    echo
    echo "Font file: $(basename "$f")"

    # Extract internal names for this font
    families=$(fc-scan --format "%{family}\n" "$f" 2>/dev/null)
    IFS=',' read -ra names <<< "$families"

    echo "  Internal font names:"
    for name in "${names[@]}"; do
        clean=$(echo "$name" | sed 's/^ *//;s/ *$//')
        echo "    - $clean"

        providers="${installed_fonts[$clean]}"

        if [[ -z "$providers" ]]; then
            echo "      No installed package provides this font name."
        else
            echo "      Found in installed packages:"
            for p in $providers; do
                echo "        - $p"
            done
        fi
        # NEW: Print Requires: font(...) for spec file
        if [[ -z "${requires_seen[$clean]}" ]]; then
            echo "      Requires: font($clean)"
            requires_seen["$clean"]=1
        fi        
    done
done

echo
echo "Done."


exit

Checking fonts provided by: python3-indico-fonts
------------------------------------------------------------
Indexing fonts from all installed packages...

Comparing fonts from python3-indico-fonts with installed packages...
------------------------------------------------------------

Font file: LiberationMono-Bold.ttf
  Found in installed packages:
    - liberation-mono-fonts-2.1.5-14.fc43.noarch
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: LiberationMono-BoldItalic.ttf
  Found in installed packages:
    - liberation-mono-fonts-2.1.5-14.fc43.noarch
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: LiberationMono-Italic.ttf
  Found in installed packages:
    - liberation-mono-fonts-2.1.5-14.fc43.noarch
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: LiberationMono-Regular.ttf
  Found in installed packages:
    - liberation-mono-fonts-2.1.5-14.fc43.noarch
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: LiberationSans-Bold.ttf
  Found in installed packages:
    - liberation-sans-fonts-2.1.5-14.fc43.noarch
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: LiberationSans-BoldItalic.ttf
  Found in installed packages:
    - liberation-sans-fonts-2.1.5-14.fc43.noarch
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: LiberationSans-Italic.ttf
  Found in installed packages:
    - liberation-sans-fonts-2.1.5-14.fc43.noarch
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: LiberationSans-Regular.ttf
  Found in installed packages:
    - liberation-sans-fonts-2.1.5-14.fc43.noarch
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: LiberationSerif-Bold.ttf
  Found in installed packages:
    - liberation-serif-fonts-2.1.5-14.fc43.noarch
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: LiberationSerif-BoldItalic.ttf
  Found in installed packages:
    - liberation-serif-fonts-2.1.5-14.fc43.noarch
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: LiberationSerif-Italic.ttf
  Found in installed packages:
    - liberation-serif-fonts-2.1.5-14.fc43.noarch
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: LiberationSerif-Regular.ttf
  Found in installed packages:
    - liberation-serif-fonts-2.1.5-14.fc43.noarch
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: LinBiolinum_R.otf
  Found in installed packages:
    - texlive-libertine-svn64359-80.fc43.noarch
    - linux-libertine-biolinum-fonts-5.3.0-32.2012_07_02.fc43.noarch
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: LinBiolinum_RB.otf
  Found in installed packages:
    - texlive-libertine-svn64359-80.fc43.noarch
    - linux-libertine-biolinum-fonts-5.3.0-32.2012_07_02.fc43.noarch
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: LinBiolinum_RI.otf
  Found in installed packages:
    - texlive-libertine-svn64359-80.fc43.noarch
    - linux-libertine-biolinum-fonts-5.3.0-32.2012_07_02.fc43.noarch
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: LinLibertine_R.otf
  Found in installed packages:
    - texlive-libertine-svn64359-80.fc43.noarch
    - linux-libertine-fonts-5.3.0-32.2012_07_02.fc43.noarch
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: LinLibertine_RB.otf
  Found in installed packages:
    - texlive-libertine-svn64359-80.fc43.noarch
    - linux-libertine-fonts-5.3.0-32.2012_07_02.fc43.noarch
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: LinLibertine_RBI.otf
  Found in installed packages:
    - texlive-libertine-svn64359-80.fc43.noarch
    - linux-libertine-fonts-5.3.0-32.2012_07_02.fc43.noarch
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: LinLibertine_RBIah.ttf   ############
  Found in installed packages:
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: LinLibertine_RBah.ttf
  Found in installed packages:
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: LinLibertine_RI.otf
  Found in installed packages:
    - texlive-libertine-svn64359-80.fc43.noarch
    - linux-libertine-fonts-5.3.0-32.2012_07_02.fc43.noarch
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: LinLibertine_RIah.ttf ############
  Found in installed packages:
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: LinLibertine_Rah.ttf            ############
  Found in installed packages:
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: NotoSansCJKjp-VF.ttf                ############ google-noto-sans-cjk-vf-fonts google-noto-sans-cjk-fonts
  Found in installed packages:
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: NotoSansMonoCJKjp-VF.ttf                            ############
  Found in installed packages:
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: NotoSerifCJKjp-VF.ttf                                  ############
  Found in installed packages:
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: kochi-gothic-subst.ttf                             ############ sazanami-gothic-fonts  due to plagiarism? 
  Found in installed packages:
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: kochi-mincho-subst.ttf                                ############ sazanami-mincho-fonts  due to plagiarism? 
  Found in installed packages:
    - python3-indico-fonts-1.2-1.fc43.noarch

Font file: uming.ttc
  Found in installed packages:
    - cjkuni-uming-fonts-0.2.20080216.2-8.fc43.noarch
    - python3-indico-fonts-1.2-1.fc43.noarch


liberation-mono-fonts
liberation-sans-fonts
liberation-serif-fonts
linux-libertine-biolinum-fonts
linux-libertine-fonts
google-noto-sans-cjk-vf-fonts 
google-noto-sans-cjk-fonts
sazanami-gothic-fonts
sazanami-mincho-fonts  
cjkuni-uming-fonts


