from ir_webstats import constants as ct
from ir_webstats.client import iRWebStats
from ir_webstats import headers as hd
from ir_webstats.util import format_results

def season_3_official_race_results(irw, custom_header=None):
    current_cust_id = irw.custid
    header, results, total_results = irw.results_archive(
        current_cust_id,
        event_types=[ct.EVENT_PRACTICE],
        season=(2020, 2, ct.ALL)
    )
    
    if custom_header is None:
        custom_header = [
            hd.START_DATE,
            hd.START_TIME,
            hd.CAR_NAME,
            hd.EVT_TYPE,
            hd.EVT_TYPE_NAME,
            hd.STARTING_POSITION,
            hd.FINISHING_POSITION,
            hd.STRENGTH_OF_FIELD
        ]
    custom_header = [str(head) for head in custom_header]
    results = format_results(results, header, custom_header)
    return results, total_results