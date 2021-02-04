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

    first_lane_name = scrapy.Field()
    first_lane_age = scrapy.Field()
    first_lane_rank = scrapy.Field()
    first_lane_motor = scrapy.Field()
    first_lane_boat = scrapy.Field()
    first_lane_weight = scrapy.Field()
    first_lane_height = scrapy.Field()
    first_lane_last_rank_1 = scrapy.Field()
    first_lane_last_rank_2 = scrapy.Field()
    first_lane_last_rank_3 = scrapy.Field()
    first_lane_top_local_perc = scrapy.Field()
    first_lane_top_national_perc = scrapy.Field()
    first_lane_top_motor_perc = scrapy.Field()
    first_lane_top_boat_perc = scrapy.Field()

    second_lane_name = scrapy.Field()
    second_lane_age = scrapy.Field()
    second_lane_rank = scrapy.Field()
    second_lane_motor = scrapy.Field()
    second_lane_boat = scrapy.Field()
    second_lane_weight = scrapy.Field()
    second_lane_height = scrapy.Field()
    second_lane_last_rank_1 = scrapy.Field()
    second_lane_last_rank_2 = scrapy.Field()
    second_lane_last_rank_3 = scrapy.Field()
    second_lane_top_local_perc = scrapy.Field()
    second_lane_top_national_perc = scrapy.Field()
    second_lane_top_motor_perc = scrapy.Field()
    second_lane_top_boat_perc = scrapy.Field()

    third_lane_name = scrapy.Field()
    third_lane_age = scrapy.Field()
    third_lane_rank = scrapy.Field()
    third_lane_motor = scrapy.Field()
    third_lane_boat = scrapy.Field()
    third_lane_weight = scrapy.Field()
    third_lane_height = scrapy.Field()
    third_lane_last_rank_1 = scrapy.Field()
    third_lane_last_rank_2 = scrapy.Field()
    third_lane_last_rank_3 = scrapy.Field()
    third_lane_top_local_perc = scrapy.Field()
    third_lane_top_national_perc = scrapy.Field()
    third_lane_top_motor_perc = scrapy.Field()
    third_lane_top_boat_perc = scrapy.Field()


    fourth_lane_name = scrapy.Field()
    fourth_lane_age = scrapy.Field()
    fourth_lane_rank = scrapy.Field()
    fourth_lane_motor = scrapy.Field()
    fourth_lane_boat = scrapy.Field()
    fourth_lane_weight = scrapy.Field()
    fourth_lane_height = scrapy.Field()
    fourth_lane_last_rank_1 = scrapy.Field()
    fourth_lane_last_rank_2 = scrapy.Field()
    fourth_lane_last_rank_3 = scrapy.Field()
    fourth_lane_top_local_perc = scrapy.Field()
    fourth_lane_top_national_perc = scrapy.Field()
    fourth_lane_top_motor_perc = scrapy.Field()
    fourth_lane_top_boat_perc = scrapy.Field()

    fifth_lane_name = scrapy.Field()
    fifth_lane_age = scrapy.Field()
    fifth_lane_rank = scrapy.Field()
    fifth_lane_motor = scrapy.Field()
    fifth_lane_boat = scrapy.Field()
    fifth_lane_weight = scrapy.Field()
    fifth_lane_height = scrapy.Field()
    fifth_lane_last_rank_1 = scrapy.Field()
    fifth_lane_last_rank_2 = scrapy.Field()
    fifth_lane_last_rank_3 = scrapy.Field()
    fifth_lane_top_local_perc = scrapy.Field()
    fifth_lane_top_national_perc = scrapy.Field()
    fifth_lane_top_motor_perc = scrapy.Field()
    fifth_lane_top_boat_perc = scrapy.Field()

    sixth_lane_name = scrapy.Field()
    sixth_lane_age = scrapy.Field()
    sixth_lane_rank = scrapy.Field()
    sixth_lane_motor = scrapy.Field()
    sixth_lane_boat = scrapy.Field()
    sixth_lane_weight = scrapy.Field()
    sixth_lane_height = scrapy.Field()
    sixth_lane_last_rank_1 = scrapy.Field()
    sixth_lane_last_rank_2 = scrapy.Field()
    sixth_lane_last_rank_3 = scrapy.Field()
    sixth_lane_top_local_perc = scrapy.Field()
    sixth_lane_top_national_perc = scrapy.Field()
    sixth_lane_top_motor_perc = scrapy.Field()
    sixth_lane_top_boat_perc = scrapy.Field()


class KyoteiSpider(scrapy.Spider):
    name = "pred"

    def start_requests(self):
        dt = '20210204'
        todays_arena = [3,4,5,7,8,18,19,20,22,23,24]
        for arena in todays_arena:
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

        item["first_lane_name"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[2]/div[1]/a/span/text()').extract()
        item["first_lane_age"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[2]/div[1]/span/text()').extract()
        item["first_lane_rank"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[4]/td[2]/table//tr[1]/td/div/span/text()').extract()
        item["first_lane_motor"] = response.xpath('//*[@id="raceTbl"]/table//tr[7]/td[2]/div[3]/text()').extract()
        item["first_lane_boat"] = response.xpath('//*[@id="raceTbl"]/table//tr[8]/td[2]/div[3]/text()').extract()
        item["first_lane_weight"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[2]/div[4]/text()').extract()
        item["first_lane_height"] = response.xpath('///*[@id="raceTbl"]/table//tr[2]/td[2]/div[3]/text()').extract()
        item["first_lane_last_rank_1"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[4]/td[2]/table//tr[2]/td[1]/span/text()').extract()
        item["first_lane_last_rank_2"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[4]/td[2]/table//tr[2]/td[2]/span/text()').extract()
        item["first_lane_last_rank_3"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[4]/td[2]/table//tr[2]/td[3]/span/text()').extract()
        item["first_lane_top_local_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[6]/td[2]/div[1]/span/text()').extract()
        item["first_lane_top_national_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[5]/td[2]/div[1]/span/text()').extract()
        item["first_lane_top_motor_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[7]/td[2]/div[1]/span/text()').extract()
        item["first_lane_top_boat_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[8]/td[2]/div[1]/span/text()').extract()

        item["second_lane_name"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[3]/div[1]/a/span/text()').extract()
        item["second_lane_age"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[3]/div[1]/span/text()').extract()
        item["second_lane_rank"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[4]/td[3]/table//tr[1]/td/div/span/text()').extract()
        item["second_lane_motor"] = response.xpath('//*[@id="raceTbl"]/table//tr[7]/td[3]/div[3]/text()').extract()
        item["second_lane_boat"] = response.xpath('//*[@id="raceTbl"]/table//tr[8]/td[3]/div[3]/text()').extract()
        item["second_lane_weight"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[3]/div[4]/text()').extract()
        item["second_lane_height"] = response.xpath('///*[@id="raceTbl"]/table//tr[2]/td[3]/div[3]/text()').extract()
        item["second_lane_last_rank_1"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[4]/td[3]/table//tr[2]/td[1]/span/text()').extract()
        item["second_lane_last_rank_2"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[4]/td[3]/table//tr[2]/td[2]/span/text()').extract()
        item["second_lane_last_rank_3"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[4]/td[3]/table//tr[2]/td[3]/span/text()').extract()
        item["second_lane_top_local_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[6]/td[3]/div[1]/span/text()').extract()
        item["second_lane_top_national_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[5]/td[3]/div[1]/span/text()').extract()
        item["second_lane_top_motor_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[7]/td[3]/div[1]/span/text()').extract()
        item["second_lane_top_boat_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[8]/td[3]/div[1]/span/text()').extract()

        item["third_lane_name"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[4]/div[1]/a/span/text()').extract()
        item["third_lane_age"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[4]/div[1]/span/text()').extract()
        item["third_lane_rank"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[4]/td[4]/table//tr[1]/td/div/span/text()').extract()
        item["third_lane_motor"] = response.xpath('//*[@id="raceTbl"]/table//tr[7]/td[4]/div[3]/text()').extract()
        item["third_lane_boat"] = response.xpath('//*[@id="raceTbl"]/table//tr[8]/td[4]/div[3]/text()').extract()
        item["third_lane_weight"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[4]/div[4]/text()').extract()
        item["third_lane_height"] = response.xpath('///*[@id="raceTbl"]/table//tr[2]/td[4]/div[3]/text()').extract()
        item["third_lane_last_rank_1"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[4]/td[4]/table//tr[2]/td[1]/span/text()').extract()
        item["third_lane_last_rank_2"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[4]/td[4]/table//tr[2]/td[2]/span/text()').extract()
        item["third_lane_last_rank_3"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[4]/td[4]/table//tr[2]/td[3]/span/text()').extract()
        item["third_lane_top_local_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[6]/td[4]/div[1]/span/text()').extract()
        item["third_lane_top_national_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[5]/td[4]/div[1]/span/text()').extract()
        item["third_lane_top_motor_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[7]/td[4]/div[1]/span/text()').extract()
        item["third_lane_top_boat_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[8]/td[4]/div[1]/span/text()').extract()

        item["fourth_lane_name"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[5]/div[1]/a/span/text()').extract()
        item["fourth_lane_age"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[5]/div[1]/span/text()').extract()
        item["fourth_lane_rank"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[4]/td[5]/table//tr[1]/td/div/span/text()').extract()
        item["fourth_lane_motor"] = response.xpath('//*[@id="raceTbl"]/table//tr[7]/td[5]/div[3]/text()').extract()
        item["fourth_lane_boat"] = response.xpath('//*[@id="raceTbl"]/table//tr[8]/td[5]/div[3]/text()').extract()
        item["fourth_lane_weight"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[5]/div[4]/text()').extract()
        item["fourth_lane_height"] = response.xpath('///*[@id="raceTbl"]/table//tr[2]/td[5]/div[3]/text()').extract()
        item["fourth_lane_last_rank_1"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[4]/td[5]/table//tr[2]/td[1]/span/text()').extract()
        item["fourth_lane_last_rank_2"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[4]/td[5]/table//tr[2]/td[2]/span/text()').extract()
        item["fourth_lane_last_rank_3"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[4]/td[5]/table//tr[2]/td[3]/span/text()').extract()
        item["fourth_lane_top_local_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[6]/td[5]/div[1]/span/text()').extract()
        item["fourth_lane_top_national_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[5]/td[5]/div[1]/span/text()').extract()
        item["fourth_lane_top_motor_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[7]/td[5]/div[1]/span/text()').extract()
        item["fourth_lane_top_boat_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[8]/td[5]/div[1]/span/text()').extract()

        item["fifth_lane_name"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[6]/div[1]/a/span/text()').extract()
        item["fifth_lane_age"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[6]/div[1]/span/text()').extract()
        item["fifth_lane_rank"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[4]/td[6]/table//tr[1]/td/div/span/text()').extract()
        item["fifth_lane_motor"] = response.xpath('//*[@id="raceTbl"]/table//tr[7]/td[6]/div[3]/text()').extract()
        item["fifth_lane_boat"] = response.xpath('//*[@id="raceTbl"]/table//tr[8]/td[6]/div[3]/text()').extract()
        item["fifth_lane_weight"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[6]/div[4]/text()').extract()
        item["fifth_lane_height"] = response.xpath('///*[@id="raceTbl"]/table//tr[2]/td[6]/div[3]/text()').extract()
        item["fifth_lane_last_rank_1"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[4]/td[6]/table//tr[2]/td[1]/span/text()').extract()
        item["fifth_lane_last_rank_2"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[4]/td[6]/table//tr[2]/td[2]/span/text()').extract()
        item["fifth_lane_last_rank_3"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[4]/td[6]/table//tr[2]/td[3]/span/text()').extract()
        item["fifth_lane_top_local_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[6]/td[6]/div[1]/span/text()').extract()
        item["fifth_lane_top_national_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[5]/td[6]/div[1]/span/text()').extract()
        item["fifth_lane_top_motor_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[7]/td[6]/div[1]/span/text()').extract()
        item["fifth_lane_top_boat_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[8]/td[6]/div[1]/span/text()').extract()

        item["sixth_lane_name"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[7]/div[1]/a/span/text()').extract()
        item["sixth_lane_age"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[7]/div[1]/span/text()').extract()
        item["sixth_lane_rank"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[4]/td[7]/table//tr[1]/td/div/span/text()').extract()
        item["sixth_lane_motor"] = response.xpath('//*[@id="raceTbl"]/table//tr[7]/td[7]/div[3]/text()').extract()
        item["sixth_lane_boat"] = response.xpath('//*[@id="raceTbl"]/table//tr[8]/td[7]/div[3]/text()').extract()
        item["sixth_lane_weight"] = response.xpath('//*[@id="raceTbl"]/table//tr[2]/td[7]/div[4]/text()').extract()
        item["sixth_lane_height"] = response.xpath('///*[@id="raceTbl"]/table//tr[2]/td[7]/div[3]/text()').extract()
        item["sixth_lane_last_rank_1"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[4]/td[7]/table//tr[2]/td[1]/span/text()').extract()
        item["sixth_lane_last_rank_2"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[4]/td[7]/table//tr[2]/td[2]/span/text()').extract()
        item["sixth_lane_last_rank_3"] = response.xpath('/html/body/div/div[2]/div[4]/div/div[2]/table//tr[4]/td[7]/table//tr[2]/td[3]/span/text()').extract()
        item["sixth_lane_top_local_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[6]/td[7]/div[1]/span/text()').extract()
        item["sixth_lane_top_national_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[5]/td[7]/div[1]/span/text()').extract()
        item["sixth_lane_top_motor_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[7]/td[7]/div[1]/span/text()').extract()
        item["sixth_lane_top_boat_perc"] = response.xpath('//*[@id="raceTbl"]/table//tr[8]/td[7]/div[1]/span/text()').extract()


        yield item
