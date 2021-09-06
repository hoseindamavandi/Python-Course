import film, series, documentary, clip

class main:
    def __init__(self):

        f = open('Data.csv')
        all_data = f.read()
        parts = all_data.split('\n')

        self.medias = []

        for i in range(len(parts)):
            info = parts[i].split(',')
            if info[1] == 'film':
                self.medias.append(film())
            
            elif info[1] == 'series':
                self.medias.append(series())
            
            elif info[1] == 'documentary':
                self.medias.append(documentary())

            elif info[1] == 'clip':
                self.medias.append(clip())

            print('✔ data loaded!')

            self.menu()

    def menu(self):    
        choose = input('1- Add New Media\n2- Edit\n3- Delete\n4- Search by name \n5- Search by duration \n6- Show Media List\n7- Show actors\n8- Download\n9- QrCode\n10- save changes and Exit\n') 
        
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
            self.makeQrcode()
        elif choose == 10:
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
           self.medias.append(film(media_info))
        elif category == 'clip':
            self.medias.append(clip(media_info))
        elif category == 'documentary':
            self.medias.append(documentary(media_info))
        elif category == 'series':
            self.medias.append(series(media_info))
        else:
            print('wrong input !')
            
        self.menu()