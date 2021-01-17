import scrapy
from datetime import date
from dateutil.rrule import rrule, DAILY


# item class included here
class RaceItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    first_lane_timing_exh = scrapy.Field()
    second_lane_timing_exh = scrapy.Field()
    third_lane_timing_exh = scrapy.Field()
    fourth_lane_timing_exh = scrapy.Field()
    fifth_lane_timing_exh = scrapy.Field()
    sixth_lane_timing_exh = scrapy.Field()
    first_lane_tilt = scrapy.Field()
    second_lane_tilt = scrapy.Field()
    third_lane_tilt = scrapy.Field()
    fourth_lane_tilt = scrapy.Field()
    fifth_lane_tilt = scrapy.Field()
    sixth_lane_tilt = scrapy.Field()
    wind_direction = scrapy.Field()
    wind_speed = scrapy.Field()
    temperature = scrapy.Field()
    weather = scrapy.Field()
    water_temp = scrapy.Field()
    wave_height = scrapy.Field()
    wave_direction = scrapy.Field()



class ExhSpider(scrapy.Spider):
    name = "exh_spider"

    def start_requests(self):
        a = date(2020, 1, 1)
        b = date(2020, 12, 23)

        for dt in rrule(DAILY, dtstart=a, until=b):
            dt = dt.strftime("%Y%m%d")
            for arena in range(1,24):
                arena = "{0:0=2d}".format(arena)
                for race_number in range(1,12):
                    url = 'http://boatrace.jp/owpc/pc/race/beforeinfo?rno={0}&jcd={1}&hd={2}'.format(race_number, arena, dt)
                    yield scrapy.Request(url=url, callback=self.parse)




    def parse(self, response):
        page = response.url.split("/")[-2]

        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

        item = RaceItem()

        item["link"] = response.url
        item["first_lane_timing_exh"] = response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[2]/div[1]/table/tbody/tr[1]/td/div/span[3]/text()').extract()
        item["second_lane_timing_exh"] = response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[2]/div[1]/table/tbody/tr[2]/td/div/span[3]/text()').extract()
        item["third_lane_timing_exh"] = response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[2]/div[1]/table/tbody/tr[3]/td/div/span[3]/text()').extract()
        item["fourth_lane_timing_exh"] = response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[2]/div[1]/table/tbody/tr[4]/td/div/span[3]/text()').extract()
        item["fifth_lane_timing_exh"] = response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[2]/div[1]/table/tbody/tr[5]/td/div/span[3]/text()').extract()
        item["sixth_lane_timing_exh"] = response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[2]/div[1]/table/tbody/tr[6]/td/div/span[3]/text()').extract()
        item["first_lane_tilt"] = response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div[1]/table/tbody[1]/tr[1]/td[6]/text()').extract()
        item["second_lane_tilt"] = response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div[1]/table/tbody[2]/tr[1]/td[6]/text()').extract()
        item["third_lane_tilt"] = response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div[1]/table/tbody[3]/tr[1]/td[6]/text()').extract()
        item["fourth_lane_tilt"] = response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div[1]/table/tbody[4]/tr[1]/td[6]/text()').extract()
        item["fifth_lane_tilt"] = response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div[1]/table/tbody[5]/tr[1]/td[6]/text()').extract()
        item["sixth_lane_tilt"] = response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[1]/div[1]/table/tbody[6]/tr[1]/td[6]/text()').extract()
        item["wind_direction"] = response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[2]/div[2]/div[1]/div[1]/p/@class').extract()
        item["wind_speed"] = response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[2]/div[2]/div[1]/div[3]/div/span[2]/text()').extract()
        item["temperature"] = response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[2]/div[2]/div[1]/div[1]/div/span[2]/text()').extract()
        item["weather"] = response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[2]/div[2]/div[1]/div[2]/div/span/text()').extract()
        item["water_temp"] = response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[2]/div[2]/div[1]/div[5]/div/span[2]/text()').extract()
        item["wave_height"] = response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[2]/div[2]/div[1]/div[6]/div/span[2]/text()').extract()
        item["wave_direction"] = response.xpath('/html/body/main/div/div/div/div[2]/div[4]/div[2]/div[2]/div[1]/div[4]/@class').extract()


        yield item
