"""백테스팅 데이터 로드 디버깅"""
import sys
from datetime import datetime, timedelta

sys.path.extend(['..', '.'])
import kis_auth as ka
from domestic_stock_functions import inquire_daily_itemchartprice

ka.auth(svr="vps")

end_date = datetime.now()
start_date = end_date - timedelta(days=365 + 100)

print("기간별시세 API 테스트")
print(f"시작일: {start_date.strftime('%Y%m%d')}")
print(f"종료일: {end_date.strftime('%Y%m%d')}")
print()

result1, result2 = inquire_daily_itemchartprice(
    env_dv="demo",
    fid_cond_mrkt_div_code="J",
    fid_input_iscd="005930",
    fid_input_date_1=start_date.strftime('%Y%m%d'),
    fid_input_date_2=end_date.strftime('%Y%m%d'),
    fid_period_div_code="D",
    fid_org_adj_prc="0"
)

print("Result1 (output1):")
print(f"  Empty: {result1.empty}")
if not result1.empty:
    print(f"  Shape: {result1.shape}")
    print(f"  Columns: {list(result1.columns)}")
    print(f"\n첫 5행:")
    print(result1.head())

print("\nResult2 (output2):")
print(f"  Empty: {result2.empty}")
if not result2.empty:
    print(f"  Shape: {result2.shape}")
    print(f"  Columns: {list(result2.columns)}")
    print(f"\n첫 5행:")
    print(result2.head())
