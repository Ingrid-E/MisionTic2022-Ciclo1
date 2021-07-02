import json

catalogue = '{"312": 1230, "94": 1545, "50": 1378, "360": 2240, "1": 1228, "37": 2009, "240": 1493}'
stickers = '312 5 57 82 500 37 1'

# catalogue = str(input())
# stickers = str(input())

def searchStickers(catalogue, stickersNeeded):
  price = 0
  stickersFound = []

  catalogue = json.loads(catalogue)
  stickersNeeded = stickersNeeded.split(' ')

  for sticker in stickersNeeded:
    if sticker in catalogue:
      price += catalogue[sticker]
      stickersFound.append(sticker)
  
  return price, stickersFound

price, stickersFound = searchStickers(catalogue, stickers)

print(price)
print(' '.join(stickersFound))
