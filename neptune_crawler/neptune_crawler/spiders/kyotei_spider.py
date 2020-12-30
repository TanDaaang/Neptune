import scrapy
from datetime import date
from dateutil.rrule import rrule, DAILY


# item class included here
class RaceItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    race_title = scrapy.Field()
    race_place = scrapy.Field()
    race_name = scrapy.Field()

    first_place_name = scrapy.Field()
    first_place_age = scrapy.Field()
    first_place_lane = scrapy.Field()
    first_place_rank = scrapy.Field()
    first_place_motor = scrapy.Field()
    first_place_boat = scrapy.Field()
    first_place_weight = scrapy.Field()
    first_place_height = scrapy.Field()
    first_place_racetime = scrapy.Field()
    first_place_timing = scrapy.Field()
    first_place_straight_time = scrapy.Field()
    first_place_last_rank_1 = scrapy.Field()
    first_place_last_rank_2 = scrapy.Field()
    first_place_last_rank_3 = scrapy.Field()
    first_place_racerid = scrapy.Field()
    first_place_top_local_perc = scrapy.Field()
    first_place_top_national_perc = scrapy.Field()
    first_place_top_motor_perc = scrapy.Field()
    first_place_top_boat_perc = scrapy.Field()

    second_place_name = scrapy.Field()
    second_place_age = scrapy.Field()
    second_place_lane = scrapy.Field()
    second_place_rank = scrapy.Field()
    second_place_motor = scrapy.Field()
    second_place_boat = scrapy.Field()
    second_place_weight = scrapy.Field()
    second_place_height = scrapy.Field()
    second_place_racetime = scrapy.Field()
    second_place_timing = scrapy.Field()
    second_place_straight_time = scrapy.Field()
    second_place_last_rank_1 = scrapy.Field()
    second_place_last_rank_2 = scrapy.Field()
    second_place_last_rank_3 = scrapy.Field()
    second_place_racerid = scrapy.Field()
    second_place_top_local_perc = scrapy.Field()
    second_place_top_national_perc = scrapy.Field()
    second_place_top_motor_perc = scrapy.Field()
    second_place_top_boat_perc = scrapy.Field()

    third_place_name = scrapy.Field()
    third_place_name = scrapy.Field()
    third_place_age = scrapy.Field()
    third_place_lane = scrapy.Field()
    third_place_rank = scrapy.Field()
    third_place_motor = scrapy.Field()
    third_place_boat = scrapy.Field()
    third_place_weight = scrapy.Field()
    third_place_height = scrapy.Field()
    third_place_racetime = scrapy.Field()
    third_place_timing = scrapy.Field()
    third_place_straight_time = scrapy.Field()
    third_place_last_rank_1 = scrapy.Field()
    third_place_last_rank_2 = scrapy.Field()
    third_place_last_rank_3 = scrapy.Field()
    third_place_racerid = scrapy.Field()
    third_place_top_local_perc = scrapy.Field()
    third_place_top_national_perc = scrapy.Field()
    third_place_top_motor_perc = scrapy.Field()
    third_place_top_boat_perc = scrapy.Field()


    fourth_place_name = scrapy.Field()
    fourth_place_name = scrapy.Field()
    fourth_place_name = scrapy.Field()
    fourth_place_age = scrapy.Field()
    fourth_place_lane = scrapy.Field()
    fourth_place_rank = scrapy.Field()
    fourth_place_motor = scrapy.Field()
    fourth_place_boat = scrapy.Field()
    fourth_place_weight = scrapy.Field()
    fourth_place_height = scrapy.Field()
    fourth_place_racetime = scrapy.Field()
    fourth_place_timing = scrapy.Field()
    fourth_place_straight_time = scrapy.Field()
    fourth_place_last_rank_1 = scrapy.Field()
    fourth_place_last_rank_2 = scrapy.Field()
    fourth_place_last_rank_3 = scrapy.Field()
    fourth_place_racerid = scrapy.Field()
    fourth_place_top_local_perc = scrapy.Field()
    fourth_place_top_national_perc = scrapy.Field()
    fourth_place_top_motor_perc = scrapy.Field()
    fourth_place_top_boat_perc = scrapy.Field()

    fifth_place_name = scrapy.Field()
    fifth_place_name = scrapy.Field()
    fifth_place_name = scrapy.Field()
    fifth_place_age = scrapy.Field()
    fifth_place_lane = scrapy.Field()
    fifth_place_rank = scrapy.Field()
    fifth_place_motor = scrapy.Field()
    fifth_place_boat = scrapy.Field()
    fifth_place_weight = scrapy.Field()
    fifth_place_height = scrapy.Field()
    fifth_place_racetime = scrapy.Field()
    fifth_place_timing = scrapy.Field()
    fifth_place_straight_time = scrapy.Field()
    fifth_place_last_rank_1 = scrapy.Field()
    fifth_place_last_rank_2 = scrapy.Field()
    fifth_place_last_rank_3 = scrapy.Field()
    fifth_place_racerid = scrapy.Field()
    fifth_place_top_local_perc = scrapy.Field()
    fifth_place_top_national_perc = scrapy.Field()
    fifth_place_top_motor_perc = scrapy.Field()
    fifth_place_top_boat_perc = scrapy.Field()

    sixth_place_name = scrapy.Field()
    sixth_place_name = scrapy.Field()
    sixth_place_name = scrapy.Field()
    sixth_place_age = scrapy.Field()
    sixth_place_lane = scrapy.Field()
    sixth_place_rank = scrapy.Field()
    sixth_place_motor = scrapy.Field()
    sixth_place_boat = scrapy.Field()
    sixth_place_weight = scrapy.Field()
    sixth_place_height = scrapy.Field()
    sixth_place_racetime = scrapy.Field()
    sixth_place_timing = scrapy.Field()
    sixth_place_straight_time = scrapy.Field()
    sixth_place_last_rank_1 = scrapy.Field()
    sixth_place_last_rank_2 = scrapy.Field()
    sixth_place_last_rank_3 = scrapy.Field()
    sixth_place_racerid = scrapy.Field()
    sixth_place_top_local_perc = scrapy.Field()
    sixth_place_top_national_perc = scrapy.Field()
    sixth_place_top_motor_perc = scrapy.Field()
    sixth_place_top_boat_perc = scrapy.Field()


class KyoteiSpider(scrapy.Spider):
    name = "kyotei"

    def start_requests(self):
        a = date(2020, 1, 1)
        b = date(2020, 12, 24)

        for dt in rrule(DAILY, dtstart=a, until=b):
            dt = dt.strftime("%Y%m%d")
            for arena in range(1,24):
                arena = "{0:0=2d}".format(arena)
                for race_number in range(1,12):
                    url = 'https://race.kyotei.club/info/info-{2}-{1}-{0}.html'.format(race_number, arena, dt)
                    yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        page = response.url.split("/")[-2]

        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

        item = RaceItem()

        item["link"] = response.url
        item["race_title"] = response.xpath('//*[@id="mainHead"]/div[1]/div/table//tr/td[3]/text()').extract()
        item["race_place"] = response.xpath('//*[@id="infoStdm"]/option[@selected="selected"]/text()').extract()
        item["race_name"] = response.xpath('/html/body/div/div[1]/div[3]/ol/li[3]/text()').extract()

        item["first_place_name"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[2]/div[1]/a/span/text()').extract()
        item["first_place_age"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[2]/div[1]/span/text()').extract()
        item["first_place_lane"] = response.xpath('//*[@id="raceTbl"]/table//tr[1]/td[2]/div/div/div/text()').extract()
        item["first_place_rank"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[2]/table//tr[1]/td/div/span/text()').extract()
        item["first_place_motor"] = response.xpath('//*[@id="raceTbl"]/table//tr[12]/td[2]/div[3]/text()').extract()
        item["first_place_boat"] = response.xpath('//*[@id="raceTbl"]/table//tr[13]/td[2]/div[3]/text()').extract()
        item["first_place_weight"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[2]/div[4]/text()').extract()
        item["first_place_height"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[2]/div[3]/text()').extract()
        item["first_place_racetime"] = list(map(str.strip, response.xpath('//*[@id="raceTbl"]/table//tr[5]/td[2]/div/text()').extract()))
        item["first_place_timing"] = response.xpath('//*[@id="raceTbl"]/table//tr[6]/td[2]/div/div[3]/text()').extract()
        item["first_place_straight_time"] = list(map(str.strip, response.xpath('//*[@id="raceTbl"]/table//tr[7]/td[2]/div/text()').extract()))
        item["first_place_last_rank_1"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[2]/table//tr[2]/td[1]/span/text()').extract()
        item["first_place_last_rank_2"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[2]/table//tr[2]/td[2]/span/text()').extract()
        item["first_place_last_rank_3"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[2]/table//tr[2]/td[3]/span/text()').extract()
        item["first_place_racerid"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[2]/div[1]/a/@href').extract()
        item["first_place_top_local_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[11]/td[2]/div[1]/span/text()').extract()
        item["first_place_top_national_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[10]/td[2]/div[1]/span/text()').extract()
        item["first_place_top_motor_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[12]/td[2]/div[1]/span/text()').extract()
        item["first_place_top_boat_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[13]/td[2]/div[1]/span/text()').extract()

        item["second_place_name"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[3]/div[1]/a/span/text()').extract()
        item["second_place_age"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[3]/div[1]/span/text()').extract()
        item["second_place_lane"] = response.xpath('//*[@id="raceTbl"]/table//tr[1]/td[3]/div/div/div/text()').extract()
        item["second_place_rank"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[3]/table//tr[1]/td/div/span/text()').extract()
        item["second_place_motor"] = response.xpath('//*[@id="raceTbl"]/table//tr[12]/td[3]/div[3]/text()').extract()
        item["second_place_boat"] = response.xpath('//*[@id="raceTbl"]/table//tr[13]/td[3]/div[3]/text()').extract()
        item["second_place_weight"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[3]/div[4]/text()').extract()
        item["second_place_height"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[3]/div[3]/text()').extract()
        item["second_place_racetime"] = list(map(str.strip, response.xpath('//*[@id="raceTbl"]/table//tr[5]/td[3]/div/text()').extract()))
        item["second_place_timing"] = response.xpath('//*[@id="raceTbl"]/table//tr[6]/td[3]/div/div[3]/text()').extract()
        item["second_place_straight_time"] = list(map(str.strip, response.xpath('//*[@id="raceTbl"]/table//tr[7]/td[3]/div/text()').extract()))
        item["second_place_last_rank_1"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[3]/table//tr[2]/td[1]/span/text()').extract()
        item["second_place_last_rank_2"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[3]/table//tr[2]/td[2]/span/text()').extract()
        item["second_place_last_rank_3"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[3]/table//tr[2]/td[3]/span/text()').extract()
        item["second_place_racerid"] = response.xpath('//*[@id="raceTbl"]/table//tr[3]/td[2]/div[1]/a/@href').extract()
        item["second_place_top_local_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[11]/td[3]/div[1]/span/text()').extract()
        item["second_place_top_national_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[10]/td[3]/div[1]/span/text()').extract()
        item["second_place_top_motor_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[12]/td[3]/div[1]/span/text()').extract()
        item["second_place_top_boat_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[13]/td[3]/div[1]/span/text()').extract()

        item["third_place_name"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[4]/div[1]/a/span/text()').extract()
        item["third_place_age"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[4]/div[1]/span/text()').extract()
        item["third_place_lane"] = response.xpath('//*[@id="raceTbl"]/table//tr[1]/td[4]/div/div/div/text()').extract()
        item["third_place_rank"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[4]/table//tr[1]/td/div/span/text()').extract()
        item["third_place_motor"] = response.xpath('//*[@id="raceTbl"]/table//tr[12]/td[4]/div[3]/text()').extract()
        item["third_place_boat"] = response.xpath('//*[@id="raceTbl"]/table//tr[13]/td[4]/div[3]/text()').extract()
        item["third_place_weight"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[4]/div[4]/text()').extract()
        item["third_place_height"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[4]/div[3]/text()').extract()
        item["third_place_racetime"] = list(map(str.strip, response.xpath('//*[@id="raceTbl"]/table//tr[5]/td[4]/div/text()').extract()))
        item["third_place_timing"] = response.xpath('//*[@id="raceTbl"]/table//tr[6]/td[4]/div/div[3]/text()').extract()
        item["third_place_straight_time"] = list(map(str.strip, response.xpath('//*[@id="raceTbl"]/table//tr[7]/td[4]/div/text()').extract()))
        item["third_place_last_rank_1"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[4]/table//tr[2]/td[1]/span/text()').extract()
        item["third_place_last_rank_2"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[4]/table//tr[2]/td[2]/span/text()').extract()
        item["third_place_last_rank_3"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[4]/table//tr[2]/td[3]/span/text()').extract()
        item["third_place_racerid"] = response.xpath('//*[@id="raceTbl"]/table//tr[3]/td[4]/div[1]/a/@href').extract()
        item["third_place_top_local_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[11]/td[4]/div[1]/span/text()').extract()
        item["third_place_top_national_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[10]/td[4]/div[1]/span/text()').extract()
        item["third_place_top_motor_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[12]/td[4]/div[1]/span/text()').extract()
        item["third_place_top_boat_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[13]/td[4]/div[1]/span/text()').extract()

        item["fourth_place_name"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[5]/div[1]/a/span/text()').extract()
        item["fourth_place_age"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[5]/div[1]/span/text()').extract()
        item["fourth_place_lane"] = response.xpath('//*[@id="raceTbl"]/table//tr[1]/td[5]/div/div/div/text()').extract()
        item["fourth_place_rank"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[5]/table//tr[1]/td/div/span/text()').extract()
        item["fourth_place_motor"] = response.xpath('//*[@id="raceTbl"]/table//tr[12]/td[5]/div[3]/text()').extract()
        item["fourth_place_boat"] = response.xpath('//*[@id="raceTbl"]/table//tr[13]/td[5]/div[3]/text()').extract()
        item["fourth_place_weight"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[5]/div[4]/text()').extract()
        item["fourth_place_height"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[5]/div[3]/text()').extract()
        item["fourth_place_racetime"] = list(map(str.strip, response.xpath('//*[@id="raceTbl"]/table//tr[5]/td[5]/div/text()').extract()))
        item["fourth_place_timing"] = response.xpath('//*[@id="raceTbl"]/table//tr[6]/td[5]/div/div[3]/text()').extract()
        item["fourth_place_straight_time"] = list(map(str.strip, response.xpath('//*[@id="raceTbl"]/table//tr[7]/td[5]/div/text()').extract()))
        item["fourth_place_last_rank_1"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[5]/table//tr[2]/td[1]/span/text()').extract()
        item["fourth_place_last_rank_2"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[5]/table//tr[2]/td[2]/span/text()').extract()
        item["fourth_place_last_rank_3"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[5]/table//tr[2]/td[3]/span/text()').extract()
        item["fourth_place_racerid"] = response.xpath('//*[@id="raceTbl"]/table//tr[3]/td[5]/div[1]/a/@href').extract()
        item["fourth_place_top_local_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[11]/td[5]/div[1]/span/text()').extract()
        item["fourth_place_top_national_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[10]/td[5]/div[1]/span/text()').extract()
        item["fourth_place_top_motor_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[12]/td[5]/div[1]/span/text()').extract()
        item["fourth_place_top_boat_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[13]/td[5]/div[1]/span/text()').extract()

        item["fifth_place_name"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[6]/div[1]/a/span/text()').extract()
        item["fifth_place_age"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[6]/div[1]/span/text()').extract()
        item["fifth_place_lane"] = response.xpath('//*[@id="raceTbl"]/table//tr[1]/td[6]/div/div/div/text()').extract()
        item["fifth_place_rank"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[6]/table//tr[1]/td/div/span/text()').extract()
        item["fifth_place_motor"] = response.xpath('//*[@id="raceTbl"]/table//tr[12]/td[6]/div[3]/text()').extract()
        item["fifth_place_boat"] = response.xpath('//*[@id="raceTbl"]/table//tr[13]/td[6]/div[3]/text()').extract()
        item["fifth_place_weight"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[6]/div[4]/text()').extract()
        item["fifth_place_height"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[6]/div[3]/text()').extract()
        item["fifth_place_racetime"] = list(map(str.strip, response.xpath('//*[@id="raceTbl"]/table//tr[5]/td[6]/div/text()').extract()))
        item["fifth_place_timing"] = response.xpath('//*[@id="raceTbl"]/table//tr[6]/td[6]/div/div[3]/text()').extract()
        item["fifth_place_straight_time"] = list(map(str.strip, response.xpath('//*[@id="raceTbl"]/table//tr[7]/td[6]/div/text()').extract()))
        item["fifth_place_last_rank_1"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[6]/table//tr[2]/td[1]/span/text()').extract()
        item["fifth_place_last_rank_2"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[6]/table//tr[2]/td[2]/span/text()').extract()
        item["fifth_place_last_rank_3"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[6]/table//tr[2]/td[3]/span/text()').extract()
        item["fifth_place_racerid"] = response.xpath('//*[@id="raceTbl"]/table//tr[3]/td[6]/div[1]/a/@href').extract()
        item["fifth_place_top_local_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[11]/td[6]/div[1]/span/text()').extract()
        item["fifth_place_top_national_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[10]/td[6]/div[1]/span/text()').extract()
        item["fifth_place_top_motor_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[12]/td[6]/div[1]/span/text()').extract()
        item["fifth_place_top_boat_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[13]/td[6]/div[1]/span/text()').extract()

        item["sixth_place_name"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[7]/div[1]/a/span/text()').extract()
        item["sixth_place_age"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[5]/div[1]/span/text()').extract()
        item["sixth_place_lane"] = response.xpath('//*[@id="raceTbl"]/table//tr[1]/td[7]/div/div/div/text()').extract()
        item["sixth_place_rank"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[7]/table//tr[1]/td/div/span/text()').extract()
        item["sixth_place_motor"] = response.xpath('//*[@id="raceTbl"]/table//tr[12]/td[7]/div[3]/text()').extract()
        item["sixth_place_boat"] = response.xpath('//*[@id="raceTbl"]/table//tr[13]/td[7]/div[3]/text()').extract()
        item["sixth_place_weight"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[7]/div[4]/text()').extract()
        item["sixth_place_height"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[7]/div[3]/text()').extract()
        item["sixth_place_racetime"] = list(map(str.strip, response.xpath('//*[@id="raceTbl"]/table//tr[5]/td[7]/div/text()').extract()))
        item["sixth_place_timing"] = response.xpath('//*[@id="raceTbl"]/table//tr[6]/td[7]/div/div[3]/text()').extract()
        item["sixth_place_straight_time"] = list(map(str.strip, response.xpath('//*[@id="raceTbl"]/table//tr[7]/td[5]/div/text()').extract()))
        item["sixth_place_last_rank_1"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[7]/table//tr[2]/td[1]/span/text()').extract()
        item["sixth_place_last_rank_2"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[7]/table//tr[2]/td[2]/span/text()').extract()
        item["sixth_place_last_rank_3"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[9]/td[7]/table//tr[2]/td[3]/span/text()').extract()
        item["sixth_place_racerid"] = response.xpath('//*[@id="raceTbl"]/table//tr[3]/td[7]/div[1]/a/@href').extract()
        item["sixth_place_top_local_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[11]/td[7]/div[1]/span/text()').extract()
        item["sixth_place_top_national_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[10]/td[7]/div[1]/span/text()').extract()
        item["sixth_place_top_motor_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[12]/td[7]/div[1]/span/text()').extract()
        item["sixth_place_top_boat_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[13]/td[7]/div[1]/span/text()').extract()

        yield item
