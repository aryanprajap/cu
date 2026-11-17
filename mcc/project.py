from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

# Initialize presentation
prs = Presentation()
prs.slide_width = Inches(13.333)  # Standard 16:9 widescreen
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

def add_header(slide, title_text, category_text="DATA PROTECTION"):
    cat_box = slide.shapes.add_textbox(Inches(1.0), Inches(0.6), Inches(11), Inches(0.4))
    tf_cat = cat_box.text_frame
    p_cat = tf_cat.paragraphs[0]
    p_cat.text = category_text.upper()
    p_cat.font.size = Pt(11)
    p_cat.font.bold = True
    p_cat.font.color.rgb = RGBColor(0, 102, 204)
    
    title_box = slide.shapes.add_textbox(Inches(1.0), Inches(0.9), Inches(11), Inches(0.8))
    tf_title = title_box.text_frame
    p_title = tf_title.paragraphs[0]
    p_title.text = title_text
    p_title.font.size = Pt(24)
    p_title.font.bold = True
    p_title.font.color.rgb = RGBColor(30, 41, 59)

# Slide 1: Title Slide
s1 = prs.slides.add_slide(blank_layout)
t_box = s1.shapes.add_textbox(Inches(1.2), Inches(2.2), Inches(11), Inches(2.5))
tf1 = t_box.text_frame
p1 = tf1.paragraphs[0]
p1.text = "Data Protection: Data at Rest, in Transit, and in Use"
p1.font.size = Pt(36)
p1.font.bold = True
p1.font.color.rgb = RGBColor(15, 23, 42)

p2 = tf1.add_paragraph()
p2.text = "Comprehensive Security Strategies Across the Full Data Lifecycle"
p2.font.size = Pt(20)
p2.font.color.rgb = RGBColor(100, 116, 139)

# Slides 2-5: Core Content Slides
content_slides = [
    ("Overview of Data Security States", [
        ("The Triad of Data States", "Data constantly moves between storage, networks, and active memory."),
        ("Why Protection Matters", "Securing data across all states prevents breaches, financial damage, and regulatory penalties."),
        ("The Shared Goal", "Achieving Confidentiality, Integrity, and Availability (CIA) regardless of data location.")
    ]),
    ("State 1: Data at Rest", [
        ("Definition", "Inactive data housed in storage (databases, local hard drives, cloud buckets, archival tapes)."),
        ("Key Risks", "Device theft, unauthorized storage access, database exploits, insider threats."),
        ("Key Controls", "Full Disk Encryption (AES-256), Key Management Services (KMS), and Role-Based Access Control (RBAC).")
    ]),
    ("State 2: Data in Transit", [
        ("Definition", "Data actively traveling across public or private networks (APIs, web traffic, emails)."),
        ("Key Risks", "Eavesdropping, packet sniffing, Man-in-the-Middle (MitM) attacks."),
        ("Key Controls", "Transport Layer Security (TLS 1.3), HTTPS, SSH/SFTP, and Virtual Private Networks (VPNs).")
    ]),
    ("State 3: Data in Use", [
        ("Definition", "Data currently being processed by RAM, CPU cache, or active application memory."),
        ("Key Risks", "Memory scraping, rootkit exploits, direct memory inspection during runtime."),
        ("Key Controls", "Confidential Computing (Hardware Enclaves / TEEs like Intel SGX / AMD SEV) and memory encryption.")
    ])
]

for title, points in content_slides:
    s = prs.slides.add_slide(blank_layout)
    add_header(s, title)
    body = s.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(11.3), Inches(4.8))
    tf = body.text_frame
    tf.word_wrap = True
    for heading, desc in points:
        p_head = tf.add_paragraph()
        p_head.text = f"•  {heading}: "
        p_head.font.bold = True
        p_head.font.size = Pt(17)
        p_head.font.color.rgb = RGBColor(30, 41, 59)
        p_head.space_before = Pt(14)
        
        # Add normal text inline
        run = p_head.add_run()
        run.text = desc
        run.font.bold = False
        run.font.size = Pt(16)
        run.font.color.rgb = RGBColor(71, 85, 105)

# Slide 6: Summary Comparison Table
s6 = prs.slides.add_slide(blank_layout)
add_header(s6, "Summary: Comparison Across States")

table_shape = s6.shapes.add_table(4, 4, Inches(1.0), Inches(2.0), Inches(11.3), Inches(4.5))
table = table_shape.table
data = [
    ["State", "Where It Resides", "Primary Threat", "Core Defense"],
    ["Data at Rest", "Databases, Disks, Cloud Storage", "Physical theft, unauthorized access", "AES-256 Encryption, RBAC"],
    ["Data in Transit", "Networks, APIs, Web Traffic", "Man-in-the-Middle, packet sniffing", "TLS/HTTPS, VPNs, SSH"],
    ["Data in Use", "RAM, CPU registers, Active Cache", "Memory scraping, insider dumping", "Confidential Computing (TEEs)"]
]

for r_idx, row in enumerate(data):
    for c_idx, val in enumerate(row):
        cell = table.cell(r_idx, c_idx)
        cell.text = val
        p = cell.text_frame.paragraphs[0]
        p.font.size = Pt(13)
        if r_idx == 0:
            p.font.bold = True
            p.font.color.rgb = RGBColor(0, 102, 204)

# Slide 7: Conclusion
s7 = prs.slides.add_slide(blank_layout)
add_header(s7, "Conclusion & Best Practices")
body7 = s7.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(11.3), Inches(4.8))
tf7 = body7.text_frame
tf7.word_wrap = True
final_points = [
    ("Defense in Depth", "Apply layered controls across all three boundaries to eliminate single points of failure."),
    ("Continuous Monitoring", "Track access logs and network metrics in real-time using SIEM platforms."),
    ("Regulatory Alignment", "Ensure continuous compliance with standards like GDPR, HIPAA, and PCI-DSS.")
]
for heading, desc in final_points:
    p_head = tf7.add_paragraph()
    p_head.text = f"•  {heading}: "
    p_head.font.bold = True
    p_head.font.size = Pt(17)
    p_head.space_before = Pt(14)
    run = p_head.add_run()
    run.text = desc
    run.font.bold = False
    run.font.size = Pt(16)

# Save the presentation
prs.save("Data_Protection_Presentation.pptx")
print("Presentation successfully created: Data_Protection_Presentation.pptx")