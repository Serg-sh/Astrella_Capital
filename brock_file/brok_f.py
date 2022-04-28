file = "20220423-01-rev00-Tr-DSKM-011121 (Transmittal) (1).zip"
file2 = "20220423-01-rev00-Tr-DSKM-011121 (Transmittal).zip"
with open(file2, 'rb') as f1:
    data1 = f1.read(1)
    data2 = f1.read()
    data_b = data2 + data1

    with open(file, 'wb') as f2:
        f2.write(data_b)
