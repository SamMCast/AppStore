# AppStore

Questions
From my experience gamers tend be very picky when it comes to buying games

I want to know how much does price, average rating, Primary Genre affect the total ratings of an app

I will restrict the data to only consider apps using US currency, that only supports one language. However, I will consider all versions of the app

I will be looking at apps with highest total ratings and then I will look at price and possibly another feature to exame the correlation it has on average rating.

The data was retrieved from [kaggle](https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps)

MobileAppStore  # The program

Optional parameters
-f # specifies the filename to read from. It could be a zipfile or CSV file. If -f is not specified than program will prompt the user for one.

-p # if you are reading from a zipfile then the parameter specifies the a password to enter if one is needed otherwise leave it blank.

## Content:
### appleStore.csv
- "id" : App ID

- "track_name": App Name

- "size_bytes": Size (in Bytes)

- "currency": Currency Type

- "price": Price amount

- "rating_count_tot": User Rating counts (for all version)

- "rating_count_ve"r": User Rating counts (for current version)

- "user_rating" : Average User Rating value (for all version)

- "user_rating_ver": Average User Rating value (for current version)

- "ver" : Latest version code

- "cont_rating": Content Rating

- "prime_genre": Primary Genre

- "sup_devices.num": Number of supporting devices

- "ipadSc_urls.num": Number of screenshots showed for display

- "lang.num": Number of supported languages

- "vpp_lic": Vpp Device Based Licensing Enabled

### appleStore_description.csv
1. id : App ID
2. track_name: Application name
3. size_bytes: Memory size (in Bytes)
4. app_desc: Application description


