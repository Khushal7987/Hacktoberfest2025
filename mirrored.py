def mirror_2d_list(image_data):
    """
    Simulates horizontally mirroring an image (a list of lists) 
    by reversing the order of elements in each row.
    """
    if not image_data or not image_data[0]:
        return []

    mirrored_data = []
    
    # Loop over every "row" (the tough part is iterating through all rows)
    for row in image_data:
        # Standard Python list slicing to reverse the order (the mirror)
        mirrored_row = row[::-1]
        mirrored_data.append(mirrored_row)
        
    return mirrored_data

# --- Usage Example ---
# A small 3x4 'image' represented by 'pixel' values (e.g., color or brightness)
simple_image = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 11, 22, 33]
]

print("Original Data (Image):")
for row in simple_image: print(row)

mirrored_result = mirror_2d_list(simple_image)

print("\nMirrored Data (Image):")
for row in mirrored_result: print(row)
