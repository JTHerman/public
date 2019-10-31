import arcpy

in_fc = input("Path to feature class: ")
date_field = input("Date field: ")
delta_field = input("Delta field: ")
date_list = []
val_list = []
i = 0
j = 0

cursor = arcpy.da.SearchCursor(in_fc, date_field)
for row in cursor:
    date_list.append(row[0])

for dt in date_list:
    if i == 0:
        c = 0
    else:
        c_dt = dt - date_list[i - 1]
        c = int(c_dt.total_seconds())
    val_list.append(c)
    i += 1

with arcpy.da.UpdateCursor(in_fc, [delta_field]) as cursor:
    for row in cursor:
        if row[0] is not None:
            pass
        else:
            row[0] = val_list[j]
            cursor.updateRow(row)
        j += 1