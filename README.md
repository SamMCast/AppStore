# AppStore

Questions
From my experience gamers tend be very picky when it comes to buying games

I want to know how much does price, average rating, Primary Genre affect the total ratings of an app

I will restrict the data to only consider apps using US currency, that only supports one language. However, I will consider all versions of the app

I will be looking at apps with highest total ratings and then I will look at price and content rating to examine the correlation it has on average rating.

The data was retrieved from [kaggle](https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps)

MobileAppStore  # The program

Optional parameters
-f # specifies the filename to read from. It could be a zipfile or CSV file. If -f is not specified than program will prompt the user for one.

-p # if you are reading from a zipfile then the parameter specifies the a password to enter if one is needed otherwise leave it blank.

## Content:
### appleStore.csv

| id | track_name | size_bytes | currency | price | rating_count_tot | rating_count_ve"r | user_rating | user_rating_ver | ver | cont_rating | prime_genre | sup_devices.num | ipadSc_urls.num | lang.num | vpp_lic |
| -- | ---------- | ---------- | -------- | ----- | ---------------- | ----------------- | ----------- | --------------- | --- | ----------- | ----------- | --------------- | --------------- | -------- | ------- |
| App ID | App Name | Size (in Bytes) | Currency Type | Price amount | User Rating counts (for all version) | User Rating counts (for current version) | Average User Rating value (for all version) | Average User Rating value (for current version) | Latest version code | Content Rating | Primary Genre | Number of supporting devices | Number of screenshots showed for display | Number of supported languages | Vpp Device Based Licensing Enabled |

### appleStore_description.csv
1. id : App ID
2. track_name: Application name
3. size_bytes: Memory size (in Bytes)
4. app_desc: Application description


