# pip install youtube_dl (at the first)
import pafy

url = input("Введите ссылку для скачивания: ")
video = pafy.new(url)

streams = video.streams
for i in streams:
   print(i)

best = video.getbest()
print(best)

best.download()
