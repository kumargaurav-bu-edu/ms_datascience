# ms_datascience
A repository to practice my learning and saving it for future

# PDF conversion 
cd week_10162026_w8/DX702O1/homework
pandoc Kumar_Gaurav_reflection5-8.md -o _tmp.html -s -c pdf_style.css --resource-path=. && \
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$(pwd)/Kumar_Gaurav_reflection5-8.pdf" \
  "file://$(pwd)/_tmp.html" && rm _tmp.html

