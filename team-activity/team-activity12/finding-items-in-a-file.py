books = []
chapters = []
volumes = []
volume_choice = int(input('''
Choose a volume:

1. Old Testament
2. New Testament
3. Book of Mormon
4. Doctrine and Covenants
5. Pearl of Great Price

Enter the number of the volume of your choice: '''))

if volume_choice == 1:
    volume_choice = 'old testament'

elif volume_choice == 2:
    volume_choice = 'new testament'

elif volume_choice == 3:
    volume_choice = 'book of mormon'

elif volume_choice == 4:
    volume_choice = 'doctrine and covenants'

elif volume_choice == 5:
    volume_choice = 'pearl of great price'

with open('./books_and_chapters.txt') as book_file:
    for line in book_file:
        parts = line.split(':')
        book_name = parts[0].strip()
        number_of_chapters = int(parts[1])
        volume = parts[2].strip()

        if volume.lower() == volume_choice:
            books.append(book_name)
            chapters.append(number_of_chapters)
            volumes.append(volume)
            # print(
            #     f'Scripture: {book_name}, Book: volume: {volume}, Chapters: {number_of_chapters}')

largest_chapter_index = chapters.index(max(chapters))

print(books[largest_chapter_index],
      chapters[largest_chapter_index], volumes[largest_chapter_index])
