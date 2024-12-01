from PIL import Image
import os

clients = [
    {
        "title": "Vinayaka Missions Kirupananda Variyar Medical College Salem",
        "slug": "vinayaka-missions-kirupananda-variyar-medical-college-salem",
        "url": "client/Vinayaka-missions-kirupananda-variyar-medical-college-salem.jpg"
    },
    {
        "title": "Vims Hospital Salem",
        "slug": "vims-hospital-salem",
        "url": "client/VIMS-hospital-Salem.png"
    },
    {
        "title": "Villupuram Govt. Medical College",
        "slug": "villupuram-govt.-medical-college",
        "url": "client/Villupuram-govt.-medical-college.jpg"
    },
    {
        "title": "Uyirthuli Blood Bank Trichy",
        "slug": "uyirthuli-blood-bank-trichy",
        "url": "client/Uyirthuli-Blood-Bank-Trichy.jpg"
    },
    {
        "title": "Tirunelveli Medical College",
        "slug": "tirunelveli-medical-college",
        "url": "client/Tirunelveli-medical-college.jpg"
    },
    {
        "title": "Thootukudi Medical College",
        "slug": "thootukudi-medical-college",
        "url": "client/Thootukudi-medical-college.jpg"
    },
    {
        "title": "Tcr Multispeciality Hospital Krishnagiri",
        "slug": "tcr-multispeciality-hospital-krishnagiri",
        "url": "client/Tcr-Multispeciality-hospital-Krishnagiri.jpg"
    },
    {
        "title": "St Joseph Hospital Dindigul",
        "slug": "st-joseph-hospital-dindigul",
        "url": "client/St-Joseph-Hospital-Dindigul.png"
    },
    {
        "title": "Sri Gokulam Hospitals Salem",
        "slug": "sri-gokulam-hospitals-salem",
        "url": "client/Sri-Gokulam-Hospitals-salem.jpg"
    },
    {
        "title": "Sks Hospital Salem",
        "slug": "sks-hospital-salem",
        "url": "client/Sks-hospital-salem.png"
    },
    {
        "title": "Shifa Hospitals Tirunelveli",
        "slug": "shifa-hospitals-tirunelveli",
        "url": "client/Shifa-Hospitals-Tirunelveli.png"
    },
    {
        "title": "Sheela Hospitals Coimbatore",
        "slug": "sheela-hospitals-coimbatore",
        "url": "client/Sheela-hospitals-Coimbatore.png"
    },
    {
        "title": "Salem Steel Plant Hospital Salem",
        "slug": "salem-steel-plant-hospital-salem",
        "url": "client/Salem-Steel-Plant-Hospital-Salem.png"
    },
    {
        "title": "Revathi Hospital Tiruppur",
        "slug": "revathi-hospital-tiruppur",
        "url": "client/Revathi-Hospital-Tiruppur.png"
    },
    {
        "title": "Ramanagounder Medical Trust Coimbatore",
        "slug": "ramanagounder-medical-trust-coimbatore",
        "url": "client/Ramanagounder-medical-trust-Coimbatore.png"
    },
    {
        "title": "Kmc Trichy",
        "slug": "kmc-trichy",
        "url": "client/KMC-Trichy.jpg"
    },
    {
        "title": "Indian Red Cross Blood Bank Thanjavur",
        "slug": "indian-red-cross-blood-bank-thanjavur",
        "url": "client/Indian-red-Cross-blood-bank-thanjavur.jpg"
    },
    {
        "title": "Gunam Hospitals Hosur",
        "slug": "gunam-hospitals-hosur",
        "url": "client/Gunam-hospitals-Hosur.png"
    },
    {
        "title": "Govt. Theni Medical College",
        "slug": "govt.-theni-medical-college",
        "url": "client/Govt.-theni-medical-college.png"
    },
    {
        "title": "Govt. Madurai Medical College",
        "slug": "govt.-madurai-medical-college",
        "url": "client/Govt.-Madurai-medical-college.jpg"
    },
    {
        "title": "Govt. Coimbatore Medical College",
        "slug": "govt.-coimbatore-medical-college",
        "url": "client/Govt.-Coimbatore-medical-college.jpg"
    },
    {
        "title": "Govt Vellore Medical College",
        "slug": "govt-vellore-medical-college",
        "url": "client/Govt-vellore-medical-college.jpg"
    },
    {
        "title": "Govt Sivagangai Medical College",
        "slug": "govt-sivagangai-medical-college",
        "url": "client/Govt-sivagangai-medical-college.jpg"
    },
    {
        "title": "Govt Salem Medical College",
        "slug": "govt-salem-medical-college",
        "url": "client/Govt-salem-medical-college.jpg"
    },
    {
        "title": "Erode Lions Blood Bank Erode",
        "slug": "erode-lions-blood-bank-erode",
        "url": "client/Erode-Lions-Blood-Bank-erode.png"
    },
    {
        "title": "Arunai Medical College Hospital Tiruvannamalai",
        "slug": "arunai-medical-college-hospital-tiruvannamalai",
        "url": "client/Arunai-Medical-college-hospital-Tiruvannamalai.png"
    },
    {
        "title": "Annapoorana Medical College Salem",
        "slug": "annapoorana-medical-college-salem",
        "url": "client/Annapoorana-Medical-College-Salem.jpg"
    }
]

def determine_class(image_path):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            aspect_ratio = width / height

            # Check conditions based on width, height, and aspect ratio
            if width > 1000 or height > 1000:
                return "col-12 col-md-8 col-lg-6 col-xl-4"  # Larger images, more space on larger screens
            elif aspect_ratio > 2:  # Extra wide image (landscape)
                return "col-12 col-md-8 col-lg-6 col-xl-4"  # Extra-wide images get more space
            elif aspect_ratio > 1.5:  # Wide image
                return "col-6 col-md-4 col-lg-3 col-xl-2"  # Wide images, smaller layout
            elif aspect_ratio < 0.75:  # Extra tall image (portrait)
                return "col-12 col-md-8 col-lg-6 col-xl-4"  # Extra-tall images get larger space
            elif height > width:  # Portrait (taller than wide)
                return "col-6 col-md-4 col-lg-3 col-xl-2"  # Portrait images
            elif width == height:  # Square images
                return "col-6 col-md-4 col-lg-3 col-xl-2"  # Square images
            elif width > height:  # Landscape (wider than tall)
                return "col-6 col-md-4 col-lg-3 col-xl-2"  # Regular landscape images
            else:  # Default case for images that don’t fit other categories
                return "col-6 col-md-4 col-lg-3 col-xl-2"
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return "col-6 col-md-4 col-lg-3 col-xl-2"  # Fallback class

# Update the clients array with the new class attribute
for client in clients:
    image_path = client["url"]
    if os.path.exists(image_path):  # Check if file exists
        client["class"] = determine_class(image_path)
    else:
        client["class"] = "col-6 col-md-4 col-lg-3 col-xl-2"  # Default class for missing files

# Output the updated clients list
for client in clients:
    print(client)
