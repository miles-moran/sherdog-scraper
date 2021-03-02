#Based on 

from ghettobird import fly

bird = {
 "url": "https://www.sherdog.com/fighter/Jon-Jones-27944",
    "flightpath": {
        "birth_date": "//span[@itemprop='birthDate']",
        "age": "//span[@class='item birthday']//strong",
        "weight_class": "//h6[@class='item wclass']//strong//a",
        "nationality": "//strong[@itemprop='nationality']",
        "camp_team": "//span[@itemprop='memberOf']//a//span",
        "locality": "//span[@itemprop='addressLocality']",
        "height_ft": "//span[@class='item height']//strong",
        "weight_lb": "//span[@class='item weight']//strong",
        "wins": "//span[./span[contains(text(),'Wins')]]//span[2]",
        "losses": "//span[./span[contains(text(),'Losses')]]//span[2]",
        "draws": "//span[./span[contains(text(),'Draws')]]//span[2]",
        "last_fight": "//span[@class='sub_line']"
    }
}

scraped = fly(bird)
print(scraped['results'])

