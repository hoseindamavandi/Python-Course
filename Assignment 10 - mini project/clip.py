from media import Media

class Clip(Media):
    def __init__(self, media):
        media.__init__(self, media[0], media[1], media[2], media[3], media[4], media[5], media[7], media[8], media[9])
        self.media = media
        self.company = media[13]
        self.duration = media[6]
        self.genre = 'genre'
        self.subject = 'subject'
        self.episode = 'episode'
        
        
    def editClip(self):
        print('which item do you want to edit?\n 1- name  2-  director  3- score  4- duration  5- url  6- info  7- category  8- company  9- year')
        selected_item = input('number of item: ')
        alternate = input('please enter alternate amount: ')
        if selected_item == '1':
            self.name = alternate
        elif selected_item == '2':
            self.director = alternate
        elif selected_item == '3':
            self.imdb_score = alternate
        elif selected_item == '4':
            self.duration= alternate
        elif selected_item == '5':
            self.url = alternate
        elif selected_item == '6':
            self.info = alternate
        elif selected_item == '7':
            self.category = alternate
        elif selected_item == '8':
            self.genre = alternate
        elif selected_item == '9':
            self.year = alternate
        else:
            print('wrong input')
        return self.media