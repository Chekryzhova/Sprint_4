import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_long_title(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби и вампиры. Восстание машин - 2')
        assert not 'Гордость и предубеждение и зомби и вампиры. Восстание машин - 2' in collector.books_genre

    @pytest.mark.parametrize(
        'title,genre',
        [
            ['Гордость и предубеждение и зомби', 'Ужасы'],
            ['Что делать, если ваш кот хочет вас убить', 'Комедии']
        ]
    )
    def test_set_book_genre_available_genres(self, title, genre):
        collector = BooksCollector()
        collector.add_new_book(title)
        collector.set_book_genre(title, genre)
        assert collector.get_book_genre(title) == genre

    def test_set_book_genre_unknown_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фэнтези')
        assert collector.get_book_genre('Властелин колец') == ''

    def test_set_book_genre_unknown_book(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Властелин колец') == ''



    def test_get_book_genre_get_one_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_get_books_with_specific_genre_get_fantastic_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Терминатор. Восстание машин')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.set_book_genre('Терминатор. Восстание машин', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Гордость и предубеждение и зомби', 'Терминатор. Восстание машин']

    def test_get_books_for_children_check_no_horrors(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Терминатор. Восстание машин')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.set_book_genre('Терминатор. Восстание машин', 'Фантастика')
        assert 'Что делать, если ваш кот хочет вас убить' not in collector.get_books_for_children()

    def test_add_book_in_favorites_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Терминатор. Восстание машин')
        collector.add_book_in_favorites('Терминатор. Восстание машин')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_list_of_favorites_books()) == 2

    def test_delete_book_from_favorites_delete_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Терминатор. Восстание машин')
        collector.add_book_in_favorites('Терминатор. Восстание машин')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert collector.get_list_of_favorites_books() == ['Терминатор. Восстание машин']





