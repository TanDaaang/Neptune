import scrapy
from datetime import date
from dateutil.rrule import rrule, DAILY


# item class included here
class RaceItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()

    first_lane_id = scrapy.Field()
    first_lane_name = scrapy.Field()
    first_lane_age = scrapy.Field()
    first_lane_rank = scrapy.Field()
    first_lane_top_local_perc_one = scrapy.Field()
    first_lane_top_local_perc_two = scrapy.Field()
    first_lane_top_local_perc_three = scrapy.Field()
    first_lane_top_national_perc_one = scrapy.Field()
    first_lane_top_national_perc_two = scrapy.Field()
    first_lane_top_national_perc_three = scrapy.Field()
    first_lane_motor = scrapy.Field()
    first_lane_top_motor_perc_two = scrapy.Field()
    first_lane_top_motor_perc_three = scrapy.Field()
    first_lane_boat = scrapy.Field()
    first_lane_top_boat_perc_two = scrapy.Field()
    first_lane_top_boat_perc_three = scrapy.Field()
    first_lane_place = scrapy.Field()

    second_lane_id = scrapy.Field()
    second_lane_name = scrapy.Field()
    second_lane_age = scrapy.Field()
    second_lane_rank = scrapy.Field()
    second_lane_top_local_perc_one = scrapy.Field()
    second_lane_top_local_perc_two = scrapy.Field()
    second_lane_top_local_perc_three = scrapy.Field()
    second_lane_top_national_perc_one = scrapy.Field()
    second_lane_top_national_perc_two = scrapy.Field()
    second_lane_top_national_perc_three = scrapy.Field()
    second_lane_motor = scrapy.Field()
    second_lane_top_motor_perc_two = scrapy.Field()
    second_lane_top_motor_perc_three = scrapy.Field()
    second_lane_boat = scrapy.Field()
    second_lane_top_boat_perc_two = scrapy.Field()
    second_lane_top_boat_perc_three = scrapy.Field()
    second_lane_place = scrapy.Field()

    third_lane_id = scrapy.Field()
    third_lane_name = scrapy.Field()
    third_lane_age = scrapy.Field()
    third_lane_rank = scrapy.Field()
    third_lane_top_local_perc_one = scrapy.Field()
    third_lane_top_local_perc_two = scrapy.Field()
    third_lane_top_local_perc_three = scrapy.Field()
    third_lane_top_national_perc_one = scrapy.Field()
    third_lane_top_national_perc_two = scrapy.Field()
    third_lane_top_national_perc_three = scrapy.Field()
    third_lane_motor = scrapy.Field()
    third_lane_top_motor_perc_two = scrapy.Field()
    third_lane_top_motor_perc_three = scrapy.Field()
    third_lane_boat = scrapy.Field()
    third_lane_top_boat_perc_two = scrapy.Field()
    third_lane_top_boat_perc_three = scrapy.Field()
    third_lane_place = scrapy.Field()

    fourth_lane_id = scrapy.Field()
    fourth_lane_name = scrapy.Field()
    fourth_lane_age = scrapy.Field()
    fourth_lane_rank = scrapy.Field()
    fourth_lane_top_local_perc_one = scrapy.Field()
    fourth_lane_top_local_perc_two = scrapy.Field()
    fourth_lane_top_local_perc_three = scrapy.Field()
    fourth_lane_top_national_perc_one = scrapy.Field()
    fourth_lane_top_national_perc_two = scrapy.Field()
    fourth_lane_top_national_perc_three = scrapy.Field()
    fourth_lane_motor = scrapy.Field()
    fourth_lane_top_motor_perc_two = scrapy.Field()
    fourth_lane_top_motor_perc_three = scrapy.Field()
    fourth_lane_boat = scrapy.Field()
    fourth_lane_top_boat_perc_two = scrapy.Field()
    fourth_lane_top_boat_perc_three = scrapy.Field()
    fourth_lane_place = scrapy.Field()

    fifth_lane_id = scrapy.Field()
    fifth_lane_name = scrapy.Field()
    fifth_lane_age = scrapy.Field()
    fifth_lane_rank = scrapy.Field()
    fifth_lane_top_local_perc_one = scrapy.Field()
    fifth_lane_top_local_perc_two = scrapy.Field()
    fifth_lane_top_local_perc_three = scrapy.Field()
    fifth_lane_top_national_perc_one = scrapy.Field()
    fifth_lane_top_national_perc_two = scrapy.Field()
    fifth_lane_top_national_perc_three = scrapy.Field()
    fifth_lane_motor = scrapy.Field()
    fifth_lane_top_motor_perc_two = scrapy.Field()
    fifth_lane_top_motor_perc_three = scrapy.Field()
    fifth_lane_boat = scrapy.Field()
    fifth_lane_top_boat_perc_two = scrapy.Field()
    fifth_lane_top_boat_perc_three = scrapy.Field()
    fifth_lane_place = scrapy.Field()

    sixth_lane_id = scrapy.Field()
    sixth_lane_name = scrapy.Field()
    sixth_lane_age = scrapy.Field()
    sixth_lane_rank = scrapy.Field()
    sixth_lane_top_local_perc_one = scrapy.Field()
    sixth_lane_top_local_perc_two = scrapy.Field()
    sixth_lane_top_local_perc_three = scrapy.Field()
    sixth_lane_top_national_perc_one = scrapy.Field()
    sixth_lane_top_national_perc_two = scrapy.Field()
    sixth_lane_top_national_perc_three = scrapy.Field()
    sixth_lane_motor = scrapy.Field()
    sixth_lane_top_motor_perc_two = scrapy.Field()
    sixth_lane_top_motor_perc_three = scrapy.Field()
    sixth_lane_boat = scrapy.Field()
    sixth_lane_top_boat_perc_two = scrapy.Field()
    sixth_lane_top_boat_perc_three = scrapy.Field()
    sixth_lane_place = scrapy.Field()


class BrSpider(scrapy.Spider):
    name = "br_spider"

    def start_requests(self):
        a = date(2020, 1, 1)
        b = date(2020, 12, 31)

        for dt in rrule(DAILY, dtstart=a, until=b):
            dt = dt.strftime("%Y%m%d")
            for arena in range(1,25):
                arena = "{0:0=2d}".format(arena)
                for race_number in range(1,13):
                    url = 'http://boatrace.jp/owpc/pc/race/racelist?rno={0}&jcd={1}&hd={2}'.format(race_number, arena, dt)
                    yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        page = response.url.split("/")[-2]

        item = RaceItem()

        item["link"] = response.url

        item["first_lane_id"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[1]/tr[1]/td[3]/div[1]/text()[1]').extract()]
        item["first_lane_name"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[1]/tr[1]/td[3]/div[2]/a/text()').extract()]
        item["first_lane_age"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[1]/tr[1]/td[3]/div[3]/text()[2]').extract()]
        item["first_lane_rank"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[1]/tr[1]/td[3]/div[1]/span/text()').extract()]
        item["first_lane_top_local_perc_one"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[1]/tr[1]/td[6]/text()[1]').extract()]
        item["first_lane_top_local_perc_two"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[1]/tr[1]/td[6]/text()[2]').extract()]
        item["first_lane_top_local_perc_three"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[1]/tr[1]/td[6]/text()[2]').extract()]
        item["first_lane_top_national_perc_one"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[1]/tr[1]/td[5]/text()[1]').extract()]
        item["first_lane_top_national_perc_two"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[1]/tr[1]/td[5]/text()[2]').extract()]
        item["first_lane_top_national_perc_three"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[1]/tr[1]/td[5]/text()[3]').extract()]
        item["first_lane_motor"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[1]/tr[1]/td[7]/text()[1]').extract()]
        item["first_lane_top_motor_perc_two"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[1]/tr[1]/td[7]/text()[2]').extract()]
        item["first_lane_top_motor_perc_three"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[1]/tr[1]/td[7]/text()[3]').extract()]
        item["first_lane_boat"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[1]/tr[1]/td[8]/text()[1]').extract()]
        item["first_lane_top_boat_perc_two"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[1]/tr[1]/td[8]/text()[2]').extract()]
        item["first_lane_top_boat_perc_three"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[1]/tr[1]/td[8]/text()[3]').extract()]

        item["second_lane_id"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[2]/tr[1]/td[3]/div[1]/text()[1]').extract()]
        item["second_lane_name"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[2]/tr[1]/td[3]/div[2]/a/text()').extract()]
        item["second_lane_age"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[2]/tr[1]/td[3]/div[3]/text()[2]').extract()]
        item["second_lane_rank"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[2]/tr[1]/td[3]/div[1]/span/text()').extract()]
        item["second_lane_top_local_perc_one"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[2]/tr[1]/td[6]/text()[1]').extract()]
        item["second_lane_top_local_perc_two"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[2]/tr[1]/td[6]/text()[2]').extract()]
        item["second_lane_top_local_perc_three"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[2]/tr[1]/td[6]/text()[2]').extract()]
        item["second_lane_top_national_perc_one"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[2]/tr[1]/td[5]/text()[1]').extract()]
        item["second_lane_top_national_perc_two"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[2]/tr[1]/td[5]/text()[2]').extract()]
        item["second_lane_top_national_perc_three"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[2]/tr[1]/td[5]/text()[3]').extract()]
        item["second_lane_motor"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[2]/tr[1]/td[7]/text()[1]').extract()]
        item["second_lane_top_motor_perc_two"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[2]/tr[1]/td[7]/text()[2]').extract()]
        item["second_lane_top_motor_perc_three"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[2]/tr[1]/td[7]/text()[3]').extract()]
        item["second_lane_boat"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[2]/tr[1]/td[8]/text()[1]').extract()]
        item["second_lane_top_boat_perc_two"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[2]/tr[1]/td[8]/text()[2]').extract()]
        item["second_lane_top_boat_perc_three"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[2]/tr[1]/td[8]/text()[3]').extract()]

        item["third_lane_id"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[3]/tr[1]/td[3]/div[1]/text()[1]').extract()]
        item["third_lane_name"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[3]/tr[1]/td[3]/div[2]/a/text()').extract()]
        item["third_lane_age"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[3]/tr[1]/td[3]/div[3]/text()[2]').extract()]
        item["third_lane_rank"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[3]/tr[1]/td[3]/div[1]/span/text()').extract()]
        item["third_lane_top_local_perc_one"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[3]/tr[1]/td[6]/text()[1]').extract()]
        item["third_lane_top_local_perc_two"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[3]/tr[1]/td[6]/text()[2]').extract()]
        item["third_lane_top_local_perc_three"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[3]/tr[1]/td[6]/text()[2]').extract()]
        item["third_lane_top_national_perc_one"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[3]/tr[1]/td[5]/text()[1]').extract()]
        item["third_lane_top_national_perc_two"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[3]/tr[1]/td[5]/text()[2]').extract()]
        item["third_lane_top_national_perc_three"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[3]/tr[1]/td[5]/text()[3]').extract()]
        item["third_lane_motor"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[3]/tr[1]/td[7]/text()[1]').extract()]
        item["third_lane_top_motor_perc_two"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[3]/tr[1]/td[7]/text()[2]').extract()]
        item["third_lane_top_motor_perc_three"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[3]/tr[1]/td[7]/text()[3]').extract()]
        item["third_lane_boat"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[3]/tr[1]/td[8]/text()[1]').extract()]
        item["third_lane_top_boat_perc_two"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[3]/tr[1]/td[8]/text()[2]').extract()]
        item["third_lane_top_boat_perc_three"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[3]/tr[1]/td[8]/text()[3]').extract()]

        item["fourth_lane_id"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[4]/tr[1]/td[3]/div[1]/text()[1]').extract()]
        item["fourth_lane_name"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[4]/tr[1]/td[3]/div[2]/a/text()').extract()]
        item["fourth_lane_age"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[4]/tr[1]/td[3]/div[3]/text()[2]').extract()]
        item["fourth_lane_rank"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[4]/tr[1]/td[3]/div[1]/span/text()').extract()]
        item["fourth_lane_top_local_perc_one"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[4]/tr[1]/td[6]/text()[1]').extract()]
        item["fourth_lane_top_local_perc_two"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[4]/tr[1]/td[6]/text()[2]').extract()]
        item["fourth_lane_top_local_perc_three"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[4]/tr[1]/td[6]/text()[2]').extract()]
        item["fourth_lane_top_national_perc_one"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[4]/tr[1]/td[5]/text()[1]').extract()]
        item["fourth_lane_top_national_perc_two"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[4]/tr[1]/td[5]/text()[2]').extract()]
        item["fourth_lane_top_national_perc_three"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[4]/tr[1]/td[5]/text()[3]').extract()]
        item["fourth_lane_motor"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[4]/tr[1]/td[7]/text()[1]').extract()]
        item["fourth_lane_top_motor_perc_two"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[4]/tr[1]/td[7]/text()[2]').extract()]
        item["fourth_lane_top_motor_perc_three"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[4]/tr[1]/td[7]/text()[3]').extract()]
        item["fourth_lane_boat"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[4]/tr[1]/td[8]/text()[1]').extract()]
        item["fourth_lane_top_boat_perc_two"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[4]/tr[1]/td[8]/text()[2]').extract()]
        item["fourth_lane_top_boat_perc_three"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[4]/tr[1]/td[8]/text()[3]').extract()]

        item["fifth_lane_id"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[5]/tr[1]/td[3]/div[1]/text()[1]').extract()]
        item["fifth_lane_name"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[5]/tr[1]/td[3]/div[2]/a/text()').extract()]
        item["fifth_lane_age"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[5]/tr[1]/td[3]/div[3]/text()[2]').extract()]
        item["fifth_lane_rank"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[5]/tr[1]/td[3]/div[1]/span/text()').extract()]
        item["fifth_lane_top_local_perc_one"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[5]/tr[1]/td[6]/text()[1]').extract()]
        item["fifth_lane_top_local_perc_two"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[5]/tr[1]/td[6]/text()[2]').extract()]
        item["fifth_lane_top_local_perc_three"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[5]/tr[1]/td[6]/text()[2]').extract()]
        item["fifth_lane_top_national_perc_one"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[5]/tr[1]/td[5]/text()[1]').extract()]
        item["fifth_lane_top_national_perc_two"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[5]/tr[1]/td[5]/text()[2]').extract()]
        item["fifth_lane_top_national_perc_three"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[5]/tr[1]/td[5]/text()[3]').extract()]
        item["fifth_lane_motor"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[5]/tr[1]/td[7]/text()[1]').extract()]
        item["fifth_lane_top_motor_perc_two"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[5]/tr[1]/td[7]/text()[2]').extract()]
        item["fifth_lane_top_motor_perc_three"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[5]/tr[1]/td[7]/text()[3]').extract()]
        item["fifth_lane_boat"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[5]/tr[1]/td[8]/text()[1]').extract()]
        item["fifth_lane_top_boat_perc_two"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[5]/tr[1]/td[8]/text()[2]').extract()]
        item["fifth_lane_top_boat_perc_three"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[5]/tr[1]/td[8]/text()[3]').extract()]

        item["sixth_lane_id"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[6]/tr[1]/td[3]/div[1]/text()[1]').extract()]
        item["sixth_lane_name"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[6]/tr[1]/td[3]/div[2]/a/text()').extract()]
        item["sixth_lane_age"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[6]/tr[1]/td[3]/div[3]/text()[2]').extract()]
        item["sixth_lane_rank"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[6]/tr[1]/td[3]/div[1]/span/text()').extract()]
        item["sixth_lane_top_local_perc_one"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[6]/tr[1]/td[6]/text()[1]').extract()]
        item["sixth_lane_top_local_perc_two"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[6]/tr[1]/td[6]/text()[2]').extract()]
        item["sixth_lane_top_local_perc_three"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[6]/tr[1]/td[6]/text()[2]').extract()]
        item["sixth_lane_top_national_perc_one"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[6]/tr[1]/td[5]/text()[1]').extract()]
        item["sixth_lane_top_national_perc_two"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[6]/tr[1]/td[5]/text()[2]').extract()]
        item["sixth_lane_top_national_perc_three"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[6]/tr[1]/td[5]/text()[3]').extract()]
        item["sixth_lane_motor"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[6]/tr[1]/td[7]/text()[1]').extract()]
        item["sixth_lane_top_motor_perc_two"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[6]/tr[1]/td[7]/text()[2]').extract()]
        item["sixth_lane_top_motor_perc_three"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[6]/tr[1]/td[7]/text()[3]').extract()]
        item["sixth_lane_boat"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[6]/tr[1]/td[8]/text()[1]').extract()]
        item["sixth_lane_top_boat_perc_two"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[6]/tr[1]/td[8]/text()[2]').extract()]
        item["sixth_lane_top_boat_perc_three"] = [item.strip() for item in response.xpath('/html/body/main/div/div/div/div[2]/div[4]/table/tbody[6]/tr[1]/td[8]/text()[3]').extract()]


        # yield item
        req = scrapy.Request(response.url.replace("racelist", "raceresult"), callback=self.parse_result)
        req.meta['data'] = item

        yield req




    def parse_result(self, response):

        item = response.meta.get('data')

        if response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[1]/tr/td[2]/text()').extract_first() == "1":
            item["first_lane_place"] = "1"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[1]/tr/td[2]/text()').extract_first() == "2":
            item["second_lane_place"] = "1"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[1]/tr/td[2]/text()').extract_first() == "3":
            item["third_lane_place"] = "1"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[1]/tr/td[2]/text()').extract_first() == "4":
            item["fourth_lane_place"] = "1"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[1]/tr/td[2]/text()').extract_first() == "5":
            item["fifth_lane_place"] = "1"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[1]/tr/td[2]/text()').extract_first() == "6":
            item["sixth_lane_place"] = "1"

        if response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[2]/tr/td[2]/text()').extract_first() == "1":
            item["first_lane_place"] = "2"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[2]/tr/td[2]/text()').extract_first() == "2":
            item["second_lane_place"] = "2"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[2]/tr/td[2]/text()').extract_first() == "3":
            item["third_lane_place"] = "2"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[2]/tr/td[2]/text()').extract_first() == "4":
            item["fourth_lane_place"] = "2"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[2]/tr/td[2]/text()').extract_first() == "5":
            item["fifth_lane_place"] = "2"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[2]/tr/td[2]/text()').extract_first() == "6":
            item["sixth_lane_place"] = "2"

        if response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[3]/tr/td[2]/text()').extract_first() == "1":
            item["first_lane_place"] = "3"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[3]/tr/td[2]/text()').extract_first() == "2":
            item["second_lane_place"] = "3"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[3]/tr/td[2]/text()').extract_first() == "3":
            item["third_lane_place"] = "3"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[3]/tr/td[2]/text()').extract_first() == "4":
            item["fourth_lane_place"] = "3"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[3]/tr/td[2]/text()').extract_first() == "5":
            item["fifth_lane_place"] = "3"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[3]/tr/td[2]/text()').extract_first() == "6":
            item["sixth_lane_place"] = "3"

        if response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[4]/tr/td[2]/text()').extract_first() == "1":
            item["first_lane_place"] = "4"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[4]/tr/td[2]/text()').extract_first() == "2":
            item["second_lane_place"] = "4"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[4]/tr/td[2]/text()').extract_first() == "3":
            item["third_lane_place"] = "4"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[4]/tr/td[2]/text()').extract_first() == "4":
            item["fourth_lane_place"] = "4"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[4]/tr/td[2]/text()').extract_first() == "5":
            item["fifth_lane_place"] = "4"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[4]/tr/td[2]/text()').extract_first() == "6":
            item["sixth_lane_place"] = "4"

        if response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[5]/tr/td[2]/text()').extract_first() == "1":
            item["first_lane_place"] = "5"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[5]/tr/td[2]/text()').extract_first() == "2":
            item["second_lane_place"] = "5"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[5]/tr/td[2]/text()').extract_first() == "3":
            item["third_lane_place"] = "5"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[5]/tr/td[2]/text()').extract_first() == "4":
            item["fourth_lane_place"] = "5"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[5]/tr/td[2]/text()').extract_first() == "5":
            item["fifth_lane_place"] = "5"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[5]/tr/td[2]/text()').extract_first() == "6":
            item["sixth_lane_place"] = "5"

        if response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[6]/tr/td[2]/text()').extract_first() == "1":
            item["first_lane_place"] = "6"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[6]/tr/td[2]/text()').extract_first() == "2":
            item["second_lane_place"] = "6"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[6]/tr/td[2]/text()').extract_first() == "3":
            item["third_lane_place"] = "6"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[6]/tr/td[2]/text()').extract_first() == "4":
            item["fourth_lane_place"] = "6"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[6]/tr/td[2]/text()').extract_first() == "5":
            item["fifth_lane_place"] = "6"
        elif response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div/table/tbody[6]/tr/td[2]/text()').extract_first() == "6":
            item["sixth_lane_place"] = "6"

        return item
