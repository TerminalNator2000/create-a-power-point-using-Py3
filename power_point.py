power_point.py

from PIL import Image

# Convert the WEBP image to PNG format
webp_image_path = "/mnt/data/A_modern,_minimalistic_logo_design_for_'Dynamic_Da.png"
png_image_path = "/mnt/data/Dynamic_Data_Solutions_Logo.png"

# Open the image and save as PNG
image = Image.open(webp_image_path)
image.save(png_image_path, "PNG")

# Now create the PowerPoint with the converted PNG image
prs = Presentation()

# Slide 1: Title Slide
slide_1 = prs.slides.add_slide(prs.slide_layouts[0])
title = slide_1.shapes.title
subtitle = slide_1.placeholders[1]
title.text = "Dynamic Data Solutions LV"
subtitle.text = "Company Logo and Concept Presentation"

# Slide 2: Introduction Slide
slide_2 = prs.slides.add_slide(prs.slide_layouts[1])
title_2 = slide_2.shapes.title
content_2 = slide_2.placeholders[1]
title_2.text = "Introduction to the Logo Concept"
content_2.text = (
    "Dynamic Data Solutions LV represents a tech-forward approach to data-driven solutions. "
    "The logo concept focuses on the following:\n\n"
    "- Modern, minimalistic design\n"
    "- Flowing lines and arrows that convey motion and dynamic data flow\n"
    "- A tech-inspired color palette to represent professionalism and trustworthiness"
)

# Slide 3: Logo Design
slide_3 = prs.slides.add_slide(prs.slide_layouts[5])
title_3 = slide_3.shapes.title
title_3.text = "Dynamic Data Solutions LV Logo"

# Add the logo image
slide_3.shapes.add_picture(png_image_path, Inches(1), Inches(1.5), width=Inches(5))

# Slide 4: Logo Concept Breakdown
slide_4 = prs.slides.add_slide(prs.slide_layouts[1])
title_4 = slide_4.shapes.title
content_4 = slide_4.placeholders[1]
title_4.text = "Logo Concept Breakdown"
content_4.text = (
    "- Abstract, flowing lines suggest dynamic motion and data flow\n"
    "- Minimalistic style maintains a clean and professional look\n"
    "- Deep blue color represents trust and reliability, while subtle gradients add modernity\n"
    "- Font hierarchy: 'Dynamic Data' is emphasized, with 'Solutions LV' in a supportive role"
)

# Slide 5: Thank You Slide
slide_5 = prs.slides.add_slide(prs.slide_layouts[1])
title_5 = slide_5.shapes.title
content_5 = slide_5.placeholders[1]
title_5.text = "Thank You!"
content_5.text = (
    "Thank you for reviewing the logo concept for Dynamic Data Solutions LV.\n\n"
    "We believe this logo embodies the innovative, data-centric approach of Dynamic Data Solutions LV. "
    "Let us know if you'd like any adjustments or additional design variations!"
)

# Save the presentation
pptx_path_updated = "/mnt/data/Dynamic_Data_Solutions_LV_Logo_Presentation_v2.pptx"
prs.save(pptx_path_updated)

pptx_path_updated
