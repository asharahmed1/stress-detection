#!/bin/bash

# Define the list of tool categories and their corresponding directories
TOOLS=(
  "vulnerability"
  "web"
  "database"
  "passwords"
  "wireless"
  "reverse-engineering"
  "exploitation"
  "social-engineering"
  "sniffing-spoofing"
  "post-exploitation"
  "forensics"
  "reporting"
)

# Define the location where the PDF files will be saved
PDF_DIR="./pdfs"

# Loop through the tool categories and create a PDF for each tool in each category
for CATEGORY in "${TOOLS[@]}"
do
  # Create a directory for the category if it doesn't exist
  if [ ! -d "$PDF_DIR/$CATEGORY" ]
  then
    mkdir -p "$PDF_DIR/$CATEGORY"
  fi

  # Loop through the tools in the category and create a PDF for each tool
  for TOOL in $(ls /usr/share/kali-linux-full/help/$CATEGORY/)
  do
    # Extract the tool's manual page and usage information
    MAN_PAGE=$(man $TOOL)
    USAGE=$(echo "$MAN_PAGE" | grep -A1 "USAGE" | tail -n1)

    # Use the tool on example.com with all available flags and options
    OUTPUT=$(echo "example.com" | $TOOL -h | xargs $TOOL)

    # Create a PDF document and add the tool information and output
    TITLE=$(echo "$MAN_PAGE" | head -n1)
    FILENAME="$PDF_DIR/$CATEGORY/$TOOL.pdf"
    printf "%s\n\n%s\n\n%s" "$TITLE" "$USAGE" "$OUTPUT" | wkhtmltopdf - $FILENAME
  done
done
