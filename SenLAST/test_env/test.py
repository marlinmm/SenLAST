
######################## COMPARISON FUNCTIONS - NEW AND STILL NOT WORKING ##########################

# def compare_date(mod_directory, sen_directory):
#     """
#     Compares the temporal (date) overlap between SENTINEL and MODIS Data
#     - For more information see: https://stackoverflow.com/questions/52464978/how-do-i-print-elements-of-one-list-that-are-in-another-list
#     """
#     date_sen_directory = sen_directory + "/selected/cloud_free"
#     date_mod_directory = mod_directory + "/cloud_free"
#
#     sentinel_date_data = extract_SENTINEL_date(sen_directory=date_sen_directory)
#     modis_date_data = extract_MODIS_date(mod_directory=date_mod_directory)
#
#     c = set(sentinel_date_data) & set(modis_date_data)
#     overlap_date_list = list(c)
#     print(overlap_date_list)
#     return overlap_date_list
#
#
# def compare_timestamp(mod_directory, sen_directory, interval):
#     """
#     Compares the temporal (time) overlap between SENTINEL and MODIS Data
#     - For more information see: https://stackoverflow.com/questions/52464978/how-do-i-print-elements-of-one-list-that-are-in-another-list
#     """
#     time_sen_directory = sen_directory + "/selected/cloud_free"
#     time_mod_directory = mod_directory + "/cloud_free"
#
#     sentinel_timestamp_data = extract_SENTINEL_timestamp(sen_directory=time_sen_directory)
#     modis_timestamp_data = extract_MODIS_timestamp(mod_directory=time_mod_directory)
#
#     overlap_time_list = [] # Die Gesamtminuten der überlappenden Szenen aus der Datumsanalyse für alle Kombinationen
#     all_minutes_overlap_list = [] # Die Minutenliste der überlappenden Szenen aus der Datumsanalyse
#
#     for u in sentinel_timestamp_data:
#         all_minutes_overlap_list.append(int(u)%60)
#
#     for x in sentinel_timestamp_data:
#         for y in modis_timestamp_data:
#             xa = int(x) + interval
#             xb = int(x) - interval
#             y = int(y)
#
#             if xa >= y >= xb:
#                 overlap_time_list.append(x)
#
#                 ### short_list ist die Liste mit den Gesamtminuten der Szenen die sich überlappen
#                 # Bin mir nicht ganz sicher, ob wir noch ne for-Schleife für das Datum brauchen, damit der nicht die
#                 # Uhrzeiten aus der short_list mit allen Datumswerten vergleicht, die in der overlap_date_list stehen
#                 short_list = list(set(overlap_time_list)) # Die Gesamtminuten der überlappenden Szenen aus der Datumsanalyse einzeln (Kurzform der overlap_time_list)
#                 min_list = [] # Minutenliste der überlappenden Szenen
#                 hr_list = [] # Stundenliste der überlappenden Szenen
#                 for t in short_list:
#                     # hr = int(t)//60
#                     min = int(t)%60
#                     # hr_list.append(hr)
#                     min_list.append(min)
#
#     print(all_minutes_overlap_list)
#     print(min_list)
#     return min_list, all_minutes_overlap_list
#
#
# # Mit Zeitkomponenete
# # FUNKTIONIERT ALLES NOCH NICHT WEIL OBEN DIE MINUTEN NOCH NICHT WIEDER UMGERECHNET SIND !!!
# def select_SENTINEL_scenes(mod_directory, sen_directory, interval):
#     new_sen_directory = sen_directory + "/selected/cloud_free"
#     new_list = extract_files_to_list(path_to_folder=new_sen_directory)
#     print(new_list)
#     overlap_date_list = compare_date(mod_directory=mod_directory, sen_directory=sen_directory)
#     min_list = compare_timestamp(mod_directory=mod_directory, sen_directory=sen_directory, interval=interval)
#     all_minutes_overlap_list = compare_timestamp(mod_directory=mod_directory, sen_directory=sen_directory, interval=interval)
#     final_tifs_selected = new_sen_directory + "/final_sentinel_selected/"
#     if os.path.exists(final_tifs_selected):
#         shutil.rmtree(final_tifs_selected)
#     os.mkdir(new_sen_directory + "/final_sentinel_selected/")
#     for h, min in enumerate(min_list):
#         for k, short in enumerate(all_minutes_overlap_list):
#             for i, element in enumerate(overlap_date_list):
#                 for j, tiff in enumerate(new_list):
#                     if min_list[k] in all_minutes_overlap_list[h]:
#                         if overlap_date_list[i] in new_list[j]:
#                             shutil.copy(new_list[j], final_tifs_selected)
#
#
# def reconversion(mod_directory, sen_directory):
#     overlap_date_list = compare_date(mod_directory=mod_directory, sen_directory=sen_directory)
#     overlap_doy_list = []
#     for a, doy in enumerate(overlap_date_list):
#         modis_date = pd.to_datetime(overlap_date_list[a], format='%Y-%m-%d')
#         modis_date_year = str(modis_date)[0:4]
#         new_year_day = pd.Timestamp(year=int(modis_date_year), month=1, day=1)
#         doy_temp = str((modis_date - new_year_day).days + 1)
#         if len(doy_temp) == 2:
#             doy_temp = "0" + doy_temp
#         overlap_doy_list.append(doy_temp)
#     return overlap_doy_list
#
#
# # Mit Zeitkomponente
# # FUNKTIONIERT SO NOCH ÜBERHAUPT NICHT WEIL ER ERST GARKEINEN ORDNER ANLEGT !!!
# def select_MODIS_scenes(mod_directory, sen_directory, interval):
#     new_mod_directory = mod_directory + "/cloud_free"
#     new_list = extract_files_to_list(path_to_folder=new_mod_directory)
#     final_tifs_selected = new_mod_directory + "/final_modis_selected/"
#     overlap_doy_list = reconversion(sen_directory=sen_directory, mod_directory=mod_directory)
#     short_list = compare_timestamp(mod_directory=mod_directory, sen_directory=sen_directory, interval=interval)
#     if os.path.exists(final_tifs_selected):
#         shutil.rmtree(final_tifs_selected)
#     os.mkdir(new_mod_directory + "/final_modis_selected/")
#     for i, element in enumerate(overlap_doy_list):
#         for j, tiff in enumerate(new_list):
#             for k, short in enumerate(short_list):
#                 if overlap_doy_list[i] in str(new_list[j]):
#                     if short_list[k] in new_list[j]:  # Voraussetzung dafür ist die Umwandlung von Gesamtminuten in Stunden und Minuten für den Layernamen
#                         shutil.copy(new_list[i], final_tifs_selected)
