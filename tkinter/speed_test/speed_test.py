import speedtest

test = speedtest.Speedtest()
down = test.download()

up = test.upload()


print('download speed', down)
print('upload speed',up)

