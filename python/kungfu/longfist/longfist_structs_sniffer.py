
# auto generated by extra_struct_info_parser.py
from ctypes import *

class XSPEED_L1_ANLIANG(Structure):
	_fields_ = [
		("exchangeID", c_char * 3),
		("validFlag", c_uint8),
		("instrumentID", c_char * 7),
		("updateTime", c_char * 9),
		("updateMillisec", c_int),
		("lastPrice", c_double),
		("matchAmount", c_int),
		("matchTotalMoney", c_double),
		("openInterest", c_double),
		("buyPrice1", c_double),
		("buyAmount1", c_int),
		("sellPrice1", c_double),
		("sellAmount1", c_int),
		]
	_pack_ = 1

class XSPEED_L2_ANLIANG(Structure):
	_fields_ = [
		("packetLen", c_int),
		("versionNo", c_ubyte),
		("updateTime", c_int),
		("exchangeID", c_char * 3),
		("instrumentID", c_char * 30),
		("stopFlag", c_bool),
		("preSettlementPrice", c_double),
		("settlementPrice", c_double),
		("averageMatchPrice", c_double),
		("yesterdayClosePrice", c_double),
		("todayClosePrice", c_double),
		("todayOpenPrice", c_double),
		("yesterdayPositionAmount", c_int),
		("positionAmount", c_int),
		("lastPrice", c_double),
		("matchAmount", c_int),
		("matchTotalMoney", c_double),
		("highestPrice", c_double),
		("lowestPrice", c_double),
		("upperPrice", c_double),
		("lowerPrice", c_double),
		("yesterdayImagineRealDegree", c_double),
		("imagineRealDegree", c_double),
		("buyPrice1", c_double),
		("sellPrice1", c_double),
		("buyAmount1", c_int),
		("sellAmount1", c_int),
		("buyPrice2", c_double),
		("sellPrice2", c_double),
		("buyAmount2", c_int),
		("sellAmount2", c_int),
		("buyPrice3", c_double),
		("sellPrice3", c_double),
		("buyAmount3", c_int),
		("sellAmount3", c_int),
		("buyPrice4", c_double),
		("sellPrice4", c_double),
		("buyAmount4", c_int),
		("sellAmount4", c_int),
		("buyPrice5", c_double),
		("sellPrice5", c_double),
		("buyAmount5", c_int),
		("sellAmount5", c_int),
		]
	_pack_ = 1

class XSPEED_L1(Structure):
	_fields_ = [
		("length", c_int32),
		("versionNo", c_ubyte),
		("updateTime", c_int32),
		("exchangeID", c_char * 3),
		("symbol", c_char * 31),
		("lastClearPrice", c_double),
		("clearPrice", c_double),
		("avgPrice", c_double),
		("lastClose", c_double),
		("todayClosePrice", c_double),
		("openPrice", c_double),
		("yesterdayPositionAmount", c_int),
		("positionAmount", c_int),
		("lastPrice", c_double),
		("matchAmount", c_int),
		("matchTotalMoney", c_double),
		("riseLimit", c_double),
		("fallLimit", c_double),
		("highPrice", c_double),
		("lowPrice", c_double),
		("yesterdayImagineRealDegree", c_double),
		("imagineRealDegree", c_double),
		("bestBidPrice", c_double),
		("bestAskPrice", c_double),
		("bestBidQty", c_int32),
		("bestAskQty", c_int32),
		]
	_pack_ = 1

class XSPEED_L2(Structure):
	_fields_ = [
		("type", c_int8),
		("__0_1", c_uint8 * 3),
		("length", c_int16),
		("__0_2", c_uint8 * 2),
		("date", c_char * 9),
		("symbol", c_char * 27),
		("symbolChineseName", c_char * 44),
		("lastPrice", c_double),
		("highPrice", c_double),
		("lowPrice", c_double),
		("lastMatchQty", c_int32),
		("matchTotQty", c_int32),
		("turnOver", c_double),
		("lastOpenInterest", c_int32),
		("openInterest", c_int32),
		("interestChange", c_int32),
		("clearPrice", c_double),
		("lifeLow", c_double),
		("lifeHigh", c_double),
		("riseLimit", c_double),
		("fallLimit", c_double),
		("lastClearPrice", c_double),
		("lastClose", c_double),
		("bestBidPrice", c_double),
		("bestBidQty", c_int16),
		("__0_3", c_uint8 * 6),
		("bestAskPrice", c_double),
		("bestAskQty", c_int16),
		("__0_4", c_uint8 * 6),
		("avgPrice", c_double),
		("time", c_char * 12),
		("__0_5", c_uint8 * 4),
		("openPrice", c_double),
		("closePrice", c_double),
		("__0_6", c_uint8 * 4),
		("bidPrice1", c_double),
		("bidVolume1", c_int16),
		("__b0_1", c_int16),
		("bidImplyQty1", c_int16),
		("__b1__", c_uint8 * 18),
		("bidPrice2", c_double),
		("bidVolume2", c_int16),
		("__b0_2", c_int16),
		("bidImplyQty2", c_int16),
		("__b2__", c_uint8 * 18),
		("bidPrice3", c_double),
		("bidVolume3", c_int16),
		("__b0_3", c_int16),
		("bidImplyQty3", c_int16),
		("__b3__", c_uint8 * 18),
		("bidPrice4", c_double),
		("bidVolume4", c_int16),
		("__b0_4", c_int16),
		("bidImplyQty4", c_int16),
		("__b4__", c_uint8 * 18),
		("bidPrice5", c_double),
		("bidVolume5", c_int16),
		("__b0_5", c_int16),
		("bidImplyQty5", c_int16),
		("__b5__", c_uint8 * 18),
		("askPrice1", c_double),
		("askVolume1", c_int16),
		("__a0_1", c_int16),
		("askImplyQty1", c_int16),
		("__a1__", c_uint8 * 18),
		("askPrice2", c_double),
		("askVolume2", c_int16),
		("__a0_2", c_int16),
		("askImplyQty2", c_int16),
		("__a2__", c_uint8 * 18),
		("askPrice3", c_double),
		("askVolume3", c_int16),
		("__a0_3", c_int16),
		("askImplyQty3", c_int16),
		("__a3__", c_uint8 * 18),
		("askPrice4", c_double),
		("askVolume4", c_int16),
		("__a0_4", c_int16),
		("askImplyQty4", c_int16),
		("__a4__", c_uint8 * 18),
		("askPrice5", c_double),
		("askVolume5", c_int16),
		("__a0_5", c_int16),
		("askImplyQty5", c_int16),
		("__a5__", c_uint8 * 18),
		("trailer", c_uint8 * 80),
		]
	_pack_ = 1

class XSPEED_L2_ORDER10(Structure):
	_fields_ = [
		("type", c_int8),
		("symbol", c_char * 27),
		("symbol_chinese_name", c_char * 56),
		("best_bid_price", c_double),
		("bid_qty_1", c_int32),
		("bid_qty_2", c_int32),
		("bid_qty_3", c_int32),
		("bid_qty_4", c_int32),
		("bid_qty_5", c_int32),
		("bid_qty_6", c_int32),
		("bid_qty_7", c_int32),
		("bid_qty_8", c_int32),
		("bid_qty_9", c_int32),
		("bid_qty_10", c_int32),
		("best_ask_price", c_double),
		("ask_qty_1", c_int32),
		("ask_qty_2", c_int32),
		("ask_qty_3", c_int32),
		("ask_qty_4", c_int32),
		("ask_qty_5", c_int32),
		("ask_qty_6", c_int32),
		("ask_qty_7", c_int32),
		("ask_qty_8", c_int32),
		("ask_qty_9", c_int32),
		("ask_qty_10", c_int32),
		("time", c_char * 16),
		("trailer", c_uint8 * 4),
		]
	_pack_ = 1

class XSPEED_L2_MATCH_BY_PRICE(Structure):
	_fields_ = [
		("type", c_int8),
		("__0_1", c_uint8 * 3),
		("symbol", c_char * 27),
		("__0_2", c_uint8 * 57),
		("match_price1", c_double),
		("buy_open_qty1", c_int),
		("buy_close_qty1", c_int),
		("sell_open_qty1", c_int),
		("sell_close_qty1", c_int),
		("match_price2", c_double),
		("buy_open_qty2", c_int),
		("buy_close_qty2", c_int),
		("sell_open_qty2", c_int),
		("sell_close_qty2", c_int),
		("match_price3", c_double),
		("buy_open_qty3", c_int),
		("buy_close_qty3", c_int),
		("sell_open_qty3", c_int),
		("sell_close_qty3", c_int),
		("match_price4", c_double),
		("buy_open_qty4", c_int),
		("buy_close_qty4", c_int),
		("sell_open_qty4", c_int),
		("sell_close_qty4", c_int),
		("match_price5", c_double),
		("buy_open_qty5", c_int),
		("buy_close_qty5", c_int),
		("sell_open_qty5", c_int),
		("sell_close_qty5", c_int),
		("trailer", c_uint8 * 4),
		]
	_pack_ = 1

class XSPEED_L2_ORDER_STATISTICS(Structure):
	_fields_ = [
		("type", c_int8),
		("__0_1", c_uint8 * 3),
		("symbol", c_char * 27),
		("__0_2", c_uint8 * 57),
		("bid_total_qty", c_int32),
		("ask_total_qty", c_int32),
		("bid_weighted_avg_price", c_double),
		("ask_weighted_avg_price", c_double),
		("trailer", c_uint8 * 4),
		]
	_pack_ = 1

class XSPEED_L2_CURRENT_SETTLE(Structure):
	_fields_ = [
		("type", c_int8),
		("__0_1", c_uint8 * 3),
		("symbol", c_char * 27),
		("__0_2", c_uint8 * 57),
		("current_settle_price", c_double),
		("trailer", c_uint8 * 4),
		]
	_pack_ = 1

class XSPEED_L2_ARB(Structure):
	_fields_ = [
		("type", c_int8),
		("__0_1", c_uint8 * 3),
		("length", c_int32),
		("date", c_char * 9),
		("symbol", c_char * 27),
		("__0_2", c_uint8 * 60),
		("last_price", c_double),
		("low_price", c_double),
		("high_price", c_double),
		("historical_low_price", c_double),
		("historical_high_price", c_double),
		("high_limit", c_double),
		("low_limit", c_double),
		("best_bid_price1", c_double),
		("best_bid_qty1", c_int32),
		("best_ask_price1", c_double),
		("best_ask_qty1", c_int32),
		("time", c_char * 12),
		("__0_3", c_uint8 * 4),
		("bid_price_1", c_double),
		("bid_volume_1", c_int32),
		("bid_imply_qty_1", c_int32),
		("__b1__", c_uint8 * 16),
		("bid_price_2", c_double),
		("bid_volume_2", c_int32),
		("bid_imply_qty_2", c_int32),
		("__b2__", c_uint8 * 16),
		("bid_price_3", c_double),
		("bid_volume_3", c_int32),
		("bid_imply_qty_3", c_int32),
		("__b3__", c_uint8 * 16),
		("bid_price_4", c_double),
		("bid_volume_4", c_int32),
		("bid_imply_qty_4", c_int32),
		("__b4__", c_uint8 * 16),
		("bid_price_5", c_double),
		("bid_volume_5", c_int32),
		("bid_imply_qty_5", c_int32),
		("__b5__", c_uint8 * 16),
		("ask_price_1", c_double),
		("ask_volume_1", c_int32),
		("ask_imply_qty_1", c_int32),
		("__a1__", c_uint8 * 16),
		("ask_price_2", c_double),
		("ask_volume_2", c_int32),
		("ask_imply_qty_2", c_int32),
		("__a2__", c_uint8 * 16),
		("ask_price_3", c_double),
		("ask_volume_3", c_int32),
		("ask_imply_qty_3", c_int32),
		("__a3__", c_uint8 * 16),
		("ask_price_4", c_double),
		("ask_volume_4", c_int32),
		("ask_imply_qty_4", c_int32),
		("__a4__", c_uint8 * 16),
		("ask_price_5", c_double),
		("ask_volume_5", c_int32),
		("ask_imply_qty_5", c_int32),
		("__a5__", c_uint8 * 16),
		("trailer", c_uint8 * 4),
		]
	_pack_ = 1

class USTP_L2(Structure):
	_fields_ = [
		("version", c_uint8),
		("chain", c_uint8),
		("_1_", c_uint8 * 22),
		("symbol", c_char * 31),
		("time", c_char * 9),
		("updateMilliSec", c_uint32),
		("_2_", c_uint8 * 4),
		("open_price", c_double),
		("highest_price", c_double),
		("lowest_price", c_double),
		("_3_", c_uint8 * 8),
		("upperlimit_price", c_double),
		("lowerlimit_price", c_double),
		("_4_", c_uint8 * 20),
		("last_price", c_double),
		("volume", c_int),
		("turnover", c_double),
		("open_interest", c_double),
		("_5_", c_uint8 * 4),
		("bid_price1", c_double),
		("bid_volume1", c_int),
		("ask_price1", c_double),
		("ask_volume1", c_int),
		("_6_", c_uint8 * 4),
		("bid_price2", c_double),
		("bid_volume2", c_int),
		("bid_price3", c_double),
		("bid_volume3", c_int),
		("_7_", c_uint8 * 4),
		("ask_price2", c_double),
		("ask_volume2", c_int),
		("ask_price3", c_double),
		("ask_volume3", c_int),
		("_8_", c_uint8 * 4),
		("bid_price4", c_double),
		("bid_volume4", c_int),
		("bid_price5", c_double),
		("bid_volume5", c_int),
		("_9_", c_uint8 * 4),
		("ask_price4", c_double),
		("ask_volume4", c_int),
		("ask_price5", c_double),
		("ask_volume5", c_int),
		]
	_pack_ = 1

class GUAVA_L1(Structure):
	_fields_ = [
		("sequence", c_uint32),
		("exchange_id", c_char),
		("channel_id", c_uint8),
		("quote_flag", c_uint8),
		("symbol", c_char * 8),
		("update_time", c_char * 9),
		("millisecond", c_int32),
		("last_px", c_double),
		("last_share", c_int32),
		("total_value", c_double),
		("total_pos", c_double),
		("bid_px", c_double),
		("bid_share", c_int32),
		("ask_px", c_double),
		("ask_share", c_int32),
		]
	_pack_ = 1

SnifferMsgType2Struct = {
	 11904 : XSPEED_L2_ANLIANG,
	 11905 : XSPEED_L2_ORDER10,
	 11906 : XSPEED_L2_MATCH_BY_PRICE,
	 11907 : XSPEED_L2_ORDER_STATISTICS,
	 11908 : XSPEED_L2_CURRENT_SETTLE,
	 11909 : XSPEED_L2_ARB,
	 11910 : USTP_L2,
	 11911 : GUAVA_L1,
	 12901 : XSPEED_L1,
	 12902 : XSPEED_L2,
	 12903 : XSPEED_L1_ANLIANG,
	 12904 : XSPEED_L2_ANLIANG,
	 12905 : XSPEED_L2_ORDER10,
	 12906 : XSPEED_L2_MATCH_BY_PRICE,
	 12907 : XSPEED_L2_ORDER_STATISTICS,
	 12908 : XSPEED_L2_CURRENT_SETTLE,
	 12909 : XSPEED_L2_ARB,
	 12910 : USTP_L2,
	 12911 : GUAVA_L1,
	 11901 : XSPEED_L1,
	 11902 : XSPEED_L2,
	 11903 : XSPEED_L1_ANLIANG,
}