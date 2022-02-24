import json
from abc import ABC, abstractmethod


class Error(Exception):
    pass

class NotValidLimit(Error):
    pass

class NotValidStatus(Error):
    pass


class StorageInJson:
    def add_log_to_json(self, request, response):
        if response != "error":
            data_to_add = {"request": request, "response": response, "status": "success"}
        else:
            data_to_add = {"request": request, "response": "", "status": "fail"}

        with open("storage.json") as json_file:
            data_from_file = json_file.read().strip()

            if not data_from_file:  # make first log
                data_from_file = [data_to_add]
                with open("storage.json", "w") as outfile:
                    json.dump(data_from_file, outfile)

            else:
                with open("storage.json") as json_file:
                    data = json.load(json_file)
                    if len(data) < 30:
                        data.append(data_to_add)
                    else:
                        data.pop(0)
                        data.append(data_to_add)

                with open("storage.json", "w") as outfile:
                    json.dump(data, outfile)

    def read_log_from_json(self, limit, status):
        with open("storage.json") as json_file:
            data = json.load(json_file)
            data.reverse()

            if status != None:
                if status in ("success", "fail"):
                    cache = []
                    for i in range(len(data)):
                        if data[i]["status"] == status:
                            cache.append(data[i])
                    data = cache
                else:
                    raise NotValidStatus

            if limit != None:
                if 1 <= limit <= 30:
                    if len(data) >= limit:
                        del data[limit:]
                    else:
                        return data
                else:
                    raise NotValidLimit

            return data


# {"request": "0.01 - 6 * 2", "response": "-11.980", "status": "success"}
# {"request": "5 + - 4", "response": "", "status": "fail"}
