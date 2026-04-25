import os

def generate_invitations(template, attendees):
    """
    Şablona əsasən iştirakçılar üçün fərdi dəvətnamələr yaradır.
    """
    # Giriş tiplərinin yoxlanılması
    if not isinstance(template, str):
        print("Error: template is not a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees is not a list of dictionaries.")
        return

    # Boş girişlərin yoxlanılması
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Hər bir iştirakçı üçün emal prosesi
    for index, attendee in enumerate(attendees, start=1):
        try:
            personalized_content = template
            # Əvəz ediləcək sahələrin siyahısı
            placeholders = ["name", "event_title", "event_date", "event_location"]
            for key in placeholders:
                # Əgər dəyər yoxdursa və ya None-dırsa "N/A" ilə əvəz et
                value = attendee.get(key)
                if value is None:
                    value = "N/A"
                personalized_content = personalized_content.replace(f"{{{key}}}", str(value))
            # Faylın adını təyin et (məsələn: output_1.txt)
            filename = f"output_{index}.txt"
            # Faylı yaz (əgər mövcud deyilsə və ya üzərinə yazmaq lazımdırsa)
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(personalized_content)
        except Exception as e:
            print(f"An error occurred while processing attendee {index}: {e}")

# Test məqsədilə nümunə şablon və məlumat (Əsas faylda istifadə üçün)
if __name__ == "__main__":
    template_str = "Hello {name},\n\nYou are invited to the {event_title} on {event_date} at {event_location}.\n\nBest regards,\nEvent Team"
    attendees_list = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]
    generate_invitations(template_str, attendees_list)
