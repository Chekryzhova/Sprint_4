# qa_python

1. Метод test_add_new_book_add_two_books проверяет, что в словарь books_genre добавилось две книги
2. Метод test_add_new_book_long_title проверяет, что книга с названием больше 40 символов не дбавляется в словарь 
3. Метод test_set_book_genre_available_genres проверяет, что добавленным в словарь книгам установились жанры
4. Метод test_set_book_genre_unknown_genre проверяет, что жанр, которого нет в списке genre не устанавливается для книги
5. Метод test_set_book_genre_unknown_book проверяет, что нельзя установить жанр для книги, которой нет в словаре
6. Метод test_get_book_genre_get_one_genre проверяет, что выводится жанр книги, которую мы указали
7. Метод test_get_books_with_specific_genre_get_fantastic_genre проверяет, что выводится список книг с жанром фантастика
8. Метод test_get_books_for_children_check_no_horrors проверяет, что в списке книг для детей нет книг с жанром ужасы
9. Метод test_add_book_in_favorites_add_two_books проверяет, что в издранное добавились две книги
10. Метод test_delete_book_from_favorites_delete_one_book проверяет, что книга удалилась из избранного