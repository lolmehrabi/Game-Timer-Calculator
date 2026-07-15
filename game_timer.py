import time

print("--- سیستم محاسبه زمان بازی ---")
input("برای شروع زمان‌گیری، کلید Enter را بزنید...")
start_time = time.time()
print("زمان‌گیری شروع شد! برای توقف کلید Enter را بزنید.")
input()
end_time = time.time()

duration = end_time - start_time
hours = duration // 3600
minutes = (duration % 3600) // 60

print(f"زمان سپری شده: {int(hours)} ساعت و {int(minutes)} دقیقه")
input("برای خروج Enter بزنید.")