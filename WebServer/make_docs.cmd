:: @echo off

for /R "static\docs" %%f in (*.md) do (
  echo Generating html for %%~nf
  copy static\docs\heading.html static\docs\%%~nf.html
  pandoc -f markdown -t html static\docs\%%~nf.md >> static\docs\%%~nf.html
  )

dir static\docs /od

