umur_3001 = int(input("Input umur anda: "))
sim_3001 = input("Apakah anda sudah punya sim C: ")[0]

if umur_3001 >= 17 and sim_3001 == 'y':
    print("Anda Sudah dewasa dan boleh bawa motor")
elif umur_3001 >= 17 and sim_3001 != 'y':
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")
elif umur_3001 < 17 and sim_3001 == 'y':
    print("Anda belum cukup umur punya SIM")
else:
    print("Anda belum cukup umur dan tidak boleh bawa motor")
print("Program Selesai")
