from clip import Clip
from media import Media
from film import Film
from series import Series
from documentary import Documentary

class main:
    def __init__(self):

        f = open('Data.csv')
        all_data = f.read()
        parts = all_data.split('\n')

        self.medias = []

        for i in range(len(parts)):
            info = parts[i].split(',')
            if info[1] == 'film':
                self.medias.append(Film())
            
            elif info[1] == 'series':
                self.medias.append(Series())
            
            elif info[1] == 'documentary':
                self.medias.append(Documentary())

            elif info[1] == 'clip':
                self.medias.append(Clip())

            print('✔ data loaded!')

            self.menu()

    def menu(self):    
        choose = input('1- Add New Media\n2- Edit\n3- Delete\n4- Search by name \n5- Search by duration \n6- Show Media List\n7- Show actors\n8- Download\n9- save changes and Exit\n') 
        
        if choose == 1:
            self.AddMedia()
        elif choose == 2:
            self.EditMedia()
        elif choose == 3:
            self.DeleteMedia()
        elif choose == 4:
            self.SearchByName()
        elif choose == 5:
            self.SearchByDuration()
        elif choose == 6:
            self.ShowMediaList()
        elif choose == 7:
            self.ShowActors()
        elif choose == 8:
            self.DownloadMedia()
        elif choose == 9:
            self.SaveAndExit()
        else:
            print('Wrong input !')

    def AddMedia(self):
        category = input('enter the category: ( film - clip - documentary - series )\n')
        id = input('id: ')
        name = input('name: ')
        year = input('year: ')
        director = input('director: ')
        score = input('score: ')
        duration = input('duration: ')
        url = input('url: ')
        info = input('info: ')
        casts = input('casts: ')
        genre = input('genre: ')
        episode = input('episode: ')
        subject = input('subject: ')
        company = input('company: ')
        media_info = [id, category, name, year, director, score, duration, url, info, casts, genre, episode, subject, company]
           
        if category == 'film':
           self.medias.append(Film(media_info))
        elif category == 'clip':
            self.medias.append(Clip(media_info))
        elif category == 'documentary':
            self.medias.append(Documentary(media_info))
        elif category == 'series':
            self.medias.append(Series(media_info))
        else:
            print('wrong input !')
            
        self.menu()

    def EditMedia(self):

        print('Editing a media:')
        name = input('enter name of media that you whant to edit:')
        for media in self.medias:
            if name == media.name:

                if media.category == 'film':
                    media = media.editFilm()
                    break
                elif media.category == 'documentary':
                    media = media.editDocumentary()
                    break
                elif media.category == 'clip':
                    media = media.editClip()
                    break
                elif media.category == 'series':
                    media = media.editSeries()
                    break
                else:
                    print('there is a problem in the data')
                    break
        else:
            print('not exists!')
        self.menu()

    def DeleteMedia(self):
        print('Deleting Media ...')
        user_input = input('please enter the name of media or id: ')

        for media in self.medias:
            if user_input == media.name or user_input == media.id:
                print('are you sure you want delete this media? \n  y?  n? ')
                yORn = input()
                if yORn == 'y':
                    self.medias.remove(media)
                    break
        else:
            print('not exists')
        self.menu()

    def SearchByName(self):

        user_input = input('enter NAME of media: ')
        for media in self.medias:
            if media.name == user_input:
                media.show()
                break
        else:
            print('not found')
        self.menu()

    def SearchByDuration(self):
        print('Search media with a specific duration')
        first_duration = input('enter first duration with format {00:00}: ')
        first_duration = first_duration.split(':')
        first_duration = [int(i) for i in first_duration]
        sec_duration = input('enter second duration with format {00:00}: ')
        sec_duration = sec_duration.split(':')
        sec_duration = [int(i) for i in sec_duration]
        for media in self.medias:
            if media.category != 'series':
                media_duration = media.duration.split(':')
                media_duration = [int(i) for i in media_duration]
                if media_duration >= first_duration and media_duration <= sec_duration:
                    media.show()
        self.menu()

    def ShowMediaList(self):
        for media in self.medias:
            media.show()
        self.menu()

    def ShowActors(self):
        user_input = input('please enter the name of media or id for show information: ')
        for media in self.medias:
            if user_input == media.name or  user_input == media.id:
                media.showCasts()
                break
        else:
            print('not exists')
        self.menu()
    
    def DownloadMedia(self):
        user_input = input('please enter the name of media or id for download: ')
        for media in self.medias:
            if user_input == media.name or  user_input == media.id:
                media.download()
                break
        else:
            print('not exists')
        self.menu()

    def SaveAndExit(self):
        out = open('Data.csv', 'w')
        for media in self.medias:
            out.write(media.id + ',' + media.category + ',' + media.name + ',' + media.year + ',' + media.director + ',' + media.imdb_score + ',' + media.duration + ',' + media.url + ',' +media.info + ',' + media.cast + ',' + media.genre + ',' + media.episode + ',' + media.subject + ',' + media.company)
            if media != self.medias[-1]:
                out.write('\n')
        out.close()
        print('Thanx! Goodbye')
        exit()



