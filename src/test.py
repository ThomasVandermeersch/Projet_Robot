import cv2
import json
import sift

def img_name_from_pkl(pkl):
    splitted = pkl.split("_")
    image_name = splitted[2] + "_" + splitted[3][:len(splitted[3])-4]
    return image_name

def spread_matches(matches):
    images = []
    scores = []
    for match in matches:
        images.append(img_name_from_pkl(match[0]))
        scores.append(match[1])
    return images, scores

#load le json
with open("src/mapping.json", "r") as map:
    mapping = json.load(map)
#get all the images name
list_name = list(mapping.keys())
test_images_folder = "src/image_test_bon/"
result = []
count_im = 0
for im_name in list_name:
    print("-------------------------")
    #read the image with opencv
    # print(test_images_folder + im_name + ".jpg")
    img = cv2.imread(test_images_folder + im_name + ".jpg")
    matches = list(sift.find_match_sift_from_pkl(img).items())[0:5] #a list of the top 5 matches
    im_refs = mapping[im_name]
    images, scores = spread_matches(matches)
    print("nombres de matchs : ",scores)
    count = 0
    best_place = -1
    for i in range(len(images)):
        # print(images[i], im_refs)
        if images[i] in im_refs:
            count += 1
            if best_place == -1:
                best_place = i
            elif scores[best_place] < scores[i]:
                best_place = i
    result.append([im_name, count, len(im_refs),best_place])
    print("image : ", result[count_im])
    count_im += 1       

conut_null = 0
best_place = []
unmatched = []
count_first = 0
for res in result:
    best_place.append(res[3])
    if res[1] == 0:
        unmatched.append(res[0])
        conut_null += 1
    if res[3] == 0:
        count_first += 1
print("--------------------------------")
print("Résumés des résultats : ")
print()
print("nombre d'images non appairées : ", conut_null)
print()
print("\nnombre d'images test : ", len(result))
print()
print("pourcentage de test concluants : ", (100-((conut_null/len(result))*100)))
print()
print("meilleures positions d'images trouvées : \n \n", best_place)
print("\nimages ayant posé problème : \n \n", unmatched)
print("\n Pourcentage de bonnes images trouvée comme plus probable : ", ((count_first/(len(best_place)-conut_null))*100))
#display the result image by image


