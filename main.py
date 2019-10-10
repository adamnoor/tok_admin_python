import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import csv
import datetime
from tkinter import *

root = Tk()
root.title('TOK Database Admin Panel')
root.geometry("600x600")


# Use a service account
cred = credentials.Certificate("./serviceAccountKey.json")
default_app = firebase_admin.initialize_app(cred)
x = datetime.datetime.now()
month = str(x.month).zfill(2)
day = str(x.day).zfill(2)
hour = str(x.hour).zfill(2)
minute = str(x.minute).zfill(2)
current_date = f"{x.year}{month}{day}"
backup_csv = f"backup_data_{current_date}_{hour}{minute}.csv"

# Player Object
class Resource:
    def __init__(self, date, kq, more, source, title, topic, media, url, link):
        self.date = date
        self.kq = kq
        self.more = more
        self.source = source
        self.title = title
        self.topic = topic
        self.media = media
        self.url = url
        self.link = link

def delete():
    
    db = firestore.client()

    db.collection(u'resources').document(delete_entry.get()).delete()

    my_label = Label(root, text=delete_entry.get() + " was sent to be deleted.  Check the database to confirm")
    my_label.pack()


def update():

    db = firestore.client()

    db_ref = db.collection(u'resources')

    csv_ref = "updated_data.csv"

    lcl_future_resources = []

    lcl_present_resources = []

    with open(csv_ref, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)  # this functions avoids the header being the first object of the list

        for line in csv_reader:
            resource: Resource = Resource(date=line[0], title=line[1], topic=line[2], kq=line[3], more=line[4],
                                          media=line[5], url=line[6], source=line[7], link=line[8])

            if resource.date is "" or resource.title is "" or resource.topic is "" or resource.kq is "" or \
                    resource.more is "" or resource.media is "" or resource.url is "" or resource.source is "" or \
                    resource.link is "":
                print(f"There's a problem with the data for {resource.title}")
            else:
                data = {
                    u'date': int(resource.date),
                    u'title': resource.title,
                    u'topic': resource.topic,
                    u'kq': resource.kq,
                    u'more': resource.more,
                    u'media': resource.media,
                    u'url': resource.url,
                    u'source': resource.source,
                    u'link': resource.link
                }

                name = data[u'title']

                if int(resource.date) > int(current_date):
                    lcl_future_resources.append(data)
                else:
                    db_ref.document(name).set(data)
                    lcl_present_resources.append(data)

        print(f"{len(lcl_present_resources)} resources have been uploaded to the database")
        print(f"{len(lcl_future_resources)} resources are set for a future date and were not uploaded to the database")
    my_label = Label(root, text="The database has been updated using updated_csv.csv")
    my_label.pack()


def backup():
    db = firestore.client()
    backup_data = backup_csv

    # future_data = "future_data.csv"

    users_ref = db.collection(u'resources')
    docs = users_ref.stream()

    with open(backup_data, 'w') as f:
        the_writer = csv.writer(f)
        the_writer.writerow(['date', 'title', 'topic', 'kq', 'more', 'media', 'url', 'source', 'link'])

        for doc in docs:
            lcl_resource = Resource(
                date=doc.get("date"),
                title=doc.get("title"),
                kq=doc.get("kq"),
                more=doc.get("more"),
                link=doc.get("link"),
                topic=doc.get("topic"),
                source=doc.get("source"),
                media=doc.get("media"),
                url=doc.get("url"),
            )
            lcl_write_array = [
                lcl_resource.date, lcl_resource.title, lcl_resource.topic, lcl_resource.kq, lcl_resource.more,
                lcl_resource.media, lcl_resource.url, lcl_resource.source, lcl_resource.link
            ]

            the_writer.writerow(lcl_write_array)
    my_label = Label(root, text="A backup has been created")
    my_label.pack()


spacer_label = Label(root, text="", padx=10, pady=10)
backup_button = Button(root, text="Backup", padx=40, pady=20, command=backup)
spacer_label2 = Label(root, text="")
update_button = Button(root, text="Update", padx=40, pady=20, command=update)
spacer_label3 = Label(root, text="")
delete_entry = Entry(root, width=25)
spacer_label4 = Label(root, text="", padx=10, pady=10)
delete_button = Button(root, text="Delete", padx=40, pady=20, command=delete)
spacer_label5 = Label(root, text="")


spacer_label.pack()
backup_button.pack()
spacer_label2.pack()
update_button.pack()
spacer_label3.pack()
delete_entry.pack()
spacer_label5.pack()
delete_button.pack()
spacer_label4.pack()
