class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("Email has been updated to {}".format(self.email))

    def __repr__(self):
        return "User: " + self.name + "; email: " + self.email + "; books read: " + str(len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, book, rating = None):
        if rating:
            self.books[book] = rating

    def get_average_rating(self):
        sum = 0
        number_of_books = len(self.books)
        for rating in self.books.values():
            sum += rating
        average_rating = sum / number_of_books
        return average_rating


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("ISBN has been updated to {}".format(str(new_isbn)))

    def add_rating(self, rating):
        if rating:
            if rating >= 0 and rating <= 4:
                self.ratings.append(rating)
            else:
                print("Invalid Rating")
              
    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_user.isbn:
            return True
        else:
            return False

    def get_average_rating(self):
        sum = 0
        number_of_ratings = len(self.ratings)
        for rating in self.ratings:
            sum += rating
        average_score = sum / number_of_ratings
        return average_score

    def __repr__(self):
        return self.title + "; " + str(self.isbn)

    def __hash__(self):
        return hash((self.title, self.isbn))


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
        
    def get_author(self):
        return self.author

    def __repr__(self):
        return self.title + " by " + self.author


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
        
    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)


class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating = None):
        wrong_email_response = "No user with email {email}".format(email = email)
        try:
            user_one = self.users[email]
            user_one.read_book(book, rating)
            book.add_rating(rating)
            if book not in self.books:
                self.books[book] = 1
            else:
                self.books[book] += 1
        except KeyError:
            print(wrong_email_response)

    def add_user(self, name, email, user_books = None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for each_book in self.books.keys():
            print(each_book)

    def print_users(self):
        for each_user in self.users.values():
            print(each_user)

    def most_read_book(self):
        maximum_reads = 0
        for each_book, number_of_reads in self.books.items():
            if number_of_reads > maximum_reads:
                maximum_reads = number_of_reads
                most_read = each_book
        return most_read

    def highest_rated_book(self):
        highest_average_rating = 0
        for each_book in self.books.keys():
            if each_book.get_average_rating() > highest_average_rating:
                highest_rated = each_book
        return highest_rated

    def most_positive_user(self):
        highest_average_rating = 0
        for each_user in self.users.values():
            if each_user.get_average_rating() > highest_average_rating:
                highest_rated =  each_user
        return each_user
              
              

























