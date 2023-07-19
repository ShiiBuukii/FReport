from lib import fb
import sys,time,getpass

f = None
def main():
	global f
	f = fb.FB()

	usr_input()

def usr_input():
	state = True
	while state:
		cmd = input("_> ")
		cmd = cmd.lower()

		if cmd == "login":
			email = input("email_> ")
			passwd = getpass.getpass("password_> ")

			res = f.login(email, passwd)
			if res[0] == True:
				print("[*] Login successfully")
				f.save_cookies()
			elif res[0] == False and res[1] == "login_checkpoint":
				print("[!] Checkpoint occured")
				code = int(input("approval_code> "))
				check_res = f.checkpoint(code)
				if check_res[0] == True:
					print("[*] Login successfully")
					f.save_cookies()
				elif check_res[0] == False and check_res[1] == "checkpoint_error":
					print("[!!] Checkpoint error, this may facebook need to confirm this device used by useragent to access.")
				else:
					print("[?] Something went wrong, but what? " + check_res[2])
			else:
				print("[?] Something went wrong, but what??? " + res[2])
		elif cmd == "cookie_login":
			f.check()
			print("[*] Current url : " + f.driver.current_url)
		elif cmd == "new_post":
			text = input("text_> ")
			res = f.new_post(text)
			if res[0] == True:
				print("[*] Post has been published ["+res[2]+"]")
			else:
				print("[!] Something went wrong : " +res[2])
		elif cmd == "report_user":
			id = input("profile_id_> ")
			count = int(input("num report_> "))
			for _ in range(count):
				res = f.report_user(id)
				if res[0] == True:
					print("[*] Report success")
				else:
					print("[!] Report error")
		elif cmd == "exit":
			state = False
			f.terminate()
			sys.exit(0)

if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(e)
		f.terminate()

# nvkbygvp@guerrillamailblock.com