import json
import datetime
def get_text(file_path):
    def time_stamp_conversion(x):
        if x > 0:
            dt = datetime.datetime.fromtimestamp(x)
            return dt
        else:
            return "Empty"

    with open(file_path, 'r') as file:
        data = json.load(file)
    def empty_folder():
        return data

    def accounts_you_re_not_interested_in():
        text = "Accounts you don't want to see in suggested posts or influence suggestions\n\n"
        for i in data["impressions_history_recs_hidden_authors"]:
            if "Username" in i["string_map_data"]:
                text += "Username: " + i["string_map_data"]["Username"]["value"]
                text += "\nTime: " + str(time_stamp_conversion(i["Time"]["timestamp"])) + "\n\n"
        return text

    def ads_viewed():
        text = "Ads you've viewed\n\n"
        for i in data["impressions_history_ads_seen"]:
            if "Author" in i["string_map_data"]:
                text += "Username: " + i["string_map_data"]["Author"]["value"]
                text += "\nTime: " + str(time_stamp_conversion(i["Time"]["timestamp"])) + "\n\n"
        return text
    
    def posts_viewed():
        text = "Posts you've viewed\n\n"
        for i in data["impressions_history_posts_seen"]:
            if "Author" in i["string_map_data"]:
                text += "Username: " + i["string_map_data"]["Author"]["value"]
                text += "\nTime: " + str(time_stamp_conversion(i["string_map_data"]["Time"]["timestamp"])) + "\n\n"
        return text

    def suggested_accounts_viewed():
        text = "Suggested accounts you've seen after following an account\n\n"
        for i in data["impressions_history_chaining_seen"]:
            if "Username" in i["string_map_data"]:
                text += "Username: " + i["string_map_data"]["Username"]["value"]
                text += "\nTime: " + str(time_stamp_conversion(i["string_map_data"]["Time"]["timestamp"])) + "\n\n"
        return text

    def videos_watched():
        text = "Videos you've watched\n\n"
        for i in data["impressions_history_videos_watched"]:
            if "Author" in i["string_map_data"]:
                text += "Username: " + i["string_map_data"]["Author"]["value"]
                text += "\nTime: " + str(time_stamp_conversion(i["string_map_data"]["Time"]["timestamp"])) + "\n\n"
        return text

    def autofill_information():
        text = "Your information Instagram has to autofill data about you\n\n"
        for key in data["ig_autofill_data"].keys():
            if data["ig_autofill_data"][key] != "": 
                text += str(key).replace("_", " ") + ": " + str(data["ig_autofill_data"][key]) + "\n"
        return text

    def post_comments():
        text = "Comments you've posted on photos and videos\n\n"
        for i in data["comments_media_comments"]:
            if "Media Owner" in i["string_map_data"]:
                text += "Name of account: " + i["string_map_data"]["Media Owner"]["value"]
                text += "\nComment: " + i["string_map_data"]["Comment"]["value"]
                text += "\nTime: " + str(time_stamp_conversion(i["string_map_data"]["Time"]["timestamp"])) + "\n\n"
        return text

    def reels_comments():
        text = "Comments you've posted on reels\n\n"
        for i in data["comments_reels_comments"]:
            if "Media Owner" in i["string_map_data"]:
                text += "Name of account: " + i["string_map_data"]["Media Owner"]["value"]
                text += "\nComment: " + i["string_map_data"]["Comment"]["value"]
                text += "\nTime: " + str(time_stamp_conversion(i["string_map_data"]["Time"]["timestamp"])) + "\n\n"
        return text

    def synced_contacts():
        text = "Contacts that have been synced\n\n"
        for i in data["contacts_contact_info"]:
            if i["string_map_data"]["First Name"]["value"] != "":
                text += "First name: " + i["string_map_data"]["First Name"]["value"] + "\n"
            if i["string_map_data"]["Last Name"]["value"] != "":
                text += "Last name: " + i["string_map_data"]["Last Name"]["value"] + "\n"
            text += "Contact information: " + i["string_map_data"]["Contact Information"]["value"] + "\n\n"
        return text

    def devices():
        text = "The devices you've used to log in and details about them\n\n"
        for i in data["devices_devices"]:
            split = i["string_map_data"]["User Agent"]["value"].split(" ")
            text += "Type of phone: "
            if split[2][0:3] == "(iP":
                text += split[2][1:7]
            else:
                text += split[2]
            text += "\nTime of last login: " + str(time_stamp_conversion(i["string_map_data"]["Last Login"]["timestamp"]))
            text += "\nDevice information: " + i["string_map_data"]["User Agent"]["value"] + "\n\n"
        return text
    def use_of_wallets_across_accounts():
        text ="Do you use wallets across accounts? "
        if data["ig_wallets_across_accounts"]:
            text += "Yes"
        else:
            text += "No"
        return text

    def accounts_you_ve_favorited():
        text = "Accounts you have selected as your favorites\n\n"
        for i in data["relationships_feed_favorites"]:
            text += "Username: " + i["string_list_data"][0]["value"]
            text += "\nLink to account: " + i["string_list_data"][0]["href"]
            text += "\nTime of adding: " + str(time_stamp_conversion(i["string_list_data"][0]["timestamp"])) + "\n\n"
        return text

    def blocked_accounts():
        text = "Accounts you have blocked\n\n"
        for i in data["relationships_blocked_users"]:
            text += "Username: " + i["title"]
            text += "\nLink to account: " + i["string_list_data"][0]["href"]
            text += "\nTime of adding: " + str(time_stamp_conversion(i["string_list_data"][0]["timestamp"])) + "\n\n"
        return text

    def follow_requests_you_ve_received():
        text = "Accounts that have requested to follow you\n\n"
        for i in data["relationships_follow_requests_received"]:
            text += "Username: " + i["string_list_data"][0]["value"]
            text += "\nLink to account: " + i["string_list_data"][0]["href"]
            text += "\nTime of request: " + str(time_stamp_conversion(i["string_list_data"][0]["timestamp"])) + "\n\n"
        return text

    def followers_1():
        text = "Accounts that follow you\n\n"
        for i in data:
            for string_data in i["string_list_data"]:
                text += "Username: " + string_data["value"]
                text += "\nLink to account: " + string_data["href"]
                text += "\nTime of adding: " + str(time_stamp_conversion(string_data["timestamp"])) + "\n\n"
        return text

    def following():
        text = "Accounts that you follow\n\n"
        for i in data["relationships_following"]:
            text += "Username: " + i["string_list_data"][0]["value"]
            text += "\nLink to account: " + i["string_list_data"][0]["href"]
            text += "\nTime of adding: " + str(time_stamp_conversion(i["string_list_data"][0]["timestamp"])) + "\n\n"
        return text

    def hide_story_from():
        text = "Accounts you have chosen to hide your stories from\n\n"
        for i in data["relationships_hide_stories_from"]:
            text += "Username: " + i["string_list_data"][0]["value"]
            text += "\nLink to account: " + i["string_list_data"][0]["href"]
            text += "\nTime of action: " + str(time_stamp_conversion(i["string_list_data"][0]["timestamp"])) + "\n\n"
        return text

    def pending_follow_requests():
        text = "Accounts who's follow request is pending\n\n"
        for i in data["relationships_follow_requests_sent"]:
            text += "Username: " + i["string_list_data"][0]["value"]
            text += "\nLink to account: " + i["string_list_data"][0]["href"]
            text += "\nTime of action: " + str(time_stamp_conversion(i["string_list_data"][0]["timestamp"])) + "\n\n"
        return text

    def recent_follow_requests():
        text = "Follow requests you've recently sent that were either confirmed or deleted\n\n"
        for i in data["relationships_permanent_follow_requests"]:
            text += "Username: " + i["string_list_data"][0]["value"]
            text += "\nLink to account: " + i["string_list_data"][0]["href"]
            text += "\nTime of action: " + str(time_stamp_conversion(i["string_list_data"][0]["timestamp"])) + "\n\n"
        return text

    def recently_unfollowed_accounts():
        text = "Accounts you have recently unfollowed\n\n"
        for i in data["relationships_unfollowed_users"]:
            text += "Username: " + i["string_list_data"][0]["value"]
            text += "\nLink to account: " + i["string_list_data"][0]["href"]
            text += "\nTime of action: " + str(time_stamp_conversion(i["string_list_data"][0]["timestamp"])) + "\n\n"
        return text

    def removed_suggestions():
        text ="Accounts that you've removed from your suggestions\n\n"
        for i in data["relationships_dismissed_suggested_users"]:
            text += "Username: " + i["string_list_data"][0]["value"]
            text += "\nLink to account: " + i["string_list_data"][0]["href"]
            text += "\nTime of action: " + str(time_stamp_conversion(i["string_list_data"][0]["timestamp"])) + "\n\n"
        return text

    def account_based_in():
        text = "Location where your account is based\n\n"
        text += data["inferred_data_primary_location"][0]["string_map_data"]["City Name"]["value"]
        return text

    def ads_interests():
        text = "Interests Instagram has gathered about you to show you relevant ads. Instagram sells you to ads that look for people with these interests.\n\n"
        for i in data["inferred_data_ig_interest"]:
            text += i["string_map_data"]["Interest"]["value"] + "\n"
        return text

    def advertisers_using_your_activity_or_information():
        text = """Advertisers using your activity or information\n
        Has data file custom audience: Indicates whether the advertiser has created a custom audience based on a data filethat includes your information, such as your email address or phone number.
        Has remarketing custom audience: Indicates whether the advertiser has created a custom audience for remarketing to you, based on your past interactions with the advertiser's website or app.
        Has in person store visit: Indicates whether the advertiser has created a custom audience based on your in-person store visits, if you have enabled location services on your Facebook account.\n\n"""
        for i in data["ig_custom_audiences_all_types"]:
            text += "Advertiser name: " + i["advertiser_name"]
            text += "\nHas data file custom audience: "
            if i["has_data_file_custom_audience"]:
                text+= "Yes"
            else:
                text+= "No"
            text += "\nHas remarketing custom audience: "
            if i["has_remarketing_custom_audience"]:
                text+= "Yes"
            else:
                text+= "No"
            text += "\nHas in person store visit: "
            if i["has_in_person_store_visit"]:
                text+= "Yes"
            else:
                text+= "No"
            text+= "\n\n\n"
        return text

    def liked_comments():
        text = "Comments you've liked\n\n"
        for i in data["likes_comment_likes"]:
            text += "Username of person who commented: " + i["title"]
            text += "\nTime of like: " + str(time_stamp_conversion(i["string_list_data"][0]["timestamp"])) + "\n\n"
        return text

    def liked_posts():
        text = "Posts you've liked\n\n"
        for i in data["likes_media_likes"]:
            text += "Username: " + i["title"]
            text += "\nTime of like: " + str(time_stamp_conversion(i["string_list_data"][0]["timestamp"])) + "\n\n"
        return text

    def account_privacy_changes():
        text = "A history of the dates and times you've updated your account's privacy\n\n"
        for i in data["account_history_account_privacy_history"]:
            text += "Action: " + i["title"]
            text += "\nDate of action: " + str(time_stamp_conversion(i["string_map_data"]["Time"]["timestamp"])) + "\n\n"
        return text

    def last_known_location():
        text = "Information about your last known location on Instagram, including imprecise GPS coordinates\n\n"
        for i in data["account_history_imprecise_last_known_location"]:
            text += "Longitude: " + i["string_map_data"]["Imprecise Longitude"]["value"]
            text += "\nLatitude: " + i["string_map_data"]["Imprecise Latitude"]["value"]
            text += "Time uploaded: " + str(time_stamp_conversion(i["string_map_data"]["Time Uploaded"]["timestamp"])) + "\n\n"
        return text

    def login_activity():
        text = "A history of your logins and associated data\n\n"
        for i in data["account_history_login_history"]:
            text += "Time of login: " + str(time_stamp_conversion(i["string_map_data"]["Time"]["timestamp"]))
            text += "\nIP address: " + i["string_map_data"]["IP Address"]["value"]
            text += "\nLanguage code: " + i["string_map_data"]["Language Code"]["value"]
            text += "\nBrowser: " + i["string_map_data"]["User Agent"]["value"] + "\n\n"
        return text

    def logout_activity():
        text = "A history of your logouts and associated data\n\n"
        for i in data["account_history_logout_history"]:
            text += "Time of login: " + str(time_stamp_conversion(i["string_map_data"]["Time"]["timestamp"]))
            text += "\nIP address: " + i["string_map_data"]["IP Address"]["value"]
            text += "\nLanguage code: " + i["string_map_data"]["Language Code"]["value"]
            text += "\nBrowser: " + i["string_map_data"]["User Agent"]["value"] + "\n\n"
        return text

    def password_change_activity():
        text = "Date and time of when your password was changed\n\n"
        for i in data["account_history_password_change_history"]:
            text += "Time: " + str(time_stamp_conversion(i["string_map_data"]["Time"]["timestamp"])) + "\n\n"
        return text

    def signup_information():
        text = "Signup information\n\n"
        for i in  data["account_history_registration_info"]:
            x = i["string_map_data"]
            if x["Username"]["value"] != "":
                text += "Username: " + x["Username"]["value"]
            if x["IP Address"]["value"] != "":
                text += "\nIP address: " + x["IP Address"]["value"]
            if x["Email"]["value"] != "":
                text += "\nEmail: " + x["Email"]["value"]
            if x["Phone Number"]["value"] != "":
                text += "\nPhone number: " + x["Phone Number"]["value"]
            if x["Device"]["value"] != "":
                text += "\nDevice: " + x["Device"]["value"]
            if x["Time"]["value"] != "":
                text += "\nTime: " + x["Time"]["value"]
        return text

    def comments_allowed_from():
        text = "Allowed from: " + data["settings_allow_comments_from"][0]["string_map_data"]["Comments Allowed From"]["value"]
        return text
    
    def use_cross_app_messaging():
        text = "Allow cross app messaging: "
        if data["settings_upgraded_to_cross_app_messaging"]["string_map_data"]["Upgraded To Cross-App Messaging"]["value"] == "True":
            text += "Yes"
        else:
            text += "No"

    def eligibility():
        text = "Information about you that Instagram uses to decide which monetization products you're eligible for\n\n"
        for i in data["monetization_eligibility"]:
            text += "Product name: " + i["string_map_data"]["Product Name"]["value"]
            text += "\nDecision: " + i["string_map_data"]["Decision"]["value"] + "\n\n"
        return text

    def account_information():
        text = "Information about your account, including settings and activity\n\n"
        for i in data["profile_account_insights"]:
            x = i["string_map_data"]
            if x["Contact Syncing"]["value"] != "":
                text += "Contact Syncing: "
                if x["Contact Syncing"]["value"] == "True":
                    text += "Yes"
                else:
                    text += "No"
            if x["First Country Code"]["value"] != "":
                text += "\nFirst country code: " + x["First Country Code"]["value"]
            if x["Has Shared Live Video"]["value"] != "":
                text += "\nHas Shared Live Video: "
                if x["Last Login"]["value"] == "True":
                    text += "Yes"
                else:
                    text += "No"
            if x["Last Login"]["timestamp"] != 0:
                text += "\nLast login: " + str(time_stamp_conversion(x["Last Login"]["timestamp"]))
            if x["Last Logout"]["timestamp"] != 0:
                text += "\nLast logout: " + str(time_stamp_conversion(x["Last Logout"]["timestamp"]))
            if x["First Story Time"]["timestamp"] != 0:
                text += "\nFirst story time: " + str(time_stamp_conversion(x["First Story Time"]["timestamp"]))
            if x["Last Story Time"]["timestamp"] != 0:
                text += "\nLast story time: " + str(time_stamp_conversion(x["Last Story Time"]["timestamp"]))
            if x["First Close Friends Story Time"]["timestamp"] != 0:
                text += "\nFirst Close Friends Story Time: " + str(time_stamp_conversion(x["First Close Friends Story Time"]["timestamp"]))
        return text

    def linked_meta_accounts():
        text = "Signup information\n\n"
        for i in  data["profile_linked_meta_accounts"]:
            x = i["string_map_data"]
            if x["User Name"]["value"] != "":
                text += "Username: " + x["User Name"]["value"]
            if x["Account Type"]["value"] != "":
                text += "\nAccount type: " + x["Account Type"]["value"]
            if x["Email"]["value"] != "":
                text += "\nEmail: " + x["Email"]["value"]
            if x["Phone Number"]["value"] != "":
                text += "\nPhone number: " + x["Phone Number"]["value"] + "\n\n"
        return text

    def personal_information():
        text = "Personal information you've added to your profile\n\n"
        for i in data["profile_user"]:
            x = i["string_map_data"]
            if x["Username"]["value"] != "":
                text += "Username: " + x["Username"]["value"]
            if x["Name"]["value"] != "":
                text += "\nName: " + x["Name"]["value"]
            if x["Email"]["value"] != "":
                text += "\nEmail: " + x["Email"]["value"]
            if x["Phone Number"]["value"] != "":
                text += "\nPhone number: " + x["Phone Number"]["value"]
            if x["Phone Confirmed"]["value"] != "":
                text += "\nPhone confirmed: "
                if x["Phone Confirmed"]["value"] == "True":
                    text += "Yes"
                else:
                    text += "No"
            if x["Phone Confirmation Method"]["value"] != "":
                text += "\nConfirmation method: " + x["Phone Confirmation Method"]["value"]
            if x["Gender"]["value"] != "":
                text += "\nGender: " + x["Gender"]["value"]
            if x["Date of birth"]["value"] != "":
                text += "\nDate of birth: " + x["Date of birth"]["value"]
            if x["Private Account"]["value"] != "":
                text += "\nPrivate account: "
                if x["Private Account"]["value"] == "True":
                    text += "Yes\n\n"
                else:
                    text +="No\n\n"
        return text
    def profile_changes():
        text = "Changes that you've made to your profile\n\n"
        for i in data["profile_profile_change"]:
            text += "Changed: " + i["string_map_data"]["Changed"]["value"]
            text += "\nNew value: " + i["string_map_data"]["New Value"]["value"]
            text += "\nDate of change: " + str(time_stamp_conversion(i["string_map_data"]["Change Date"]["timestamp"])) + "\n\n"
        return text

    def notification_of_privacy_policy_updates():
        text = "History of notifications about policy updates and permissions\n\n"
        for i in data["policy_updates_and_permissions_notification_of_privacy_policy_updates"]:
            text += "Date: " + i["string_map_data"]["Impression Time"]["value"]
            text += "\nCOnsent status: " + i["string_map_data"]["Consent Status"]["value"] + "\n\n"
        return text

    def account_searches():
        text = "Accounts you've recently searched for\n\n"
        for i in data["searches_user"]:
            text += "Username: " + i["string_map_data"]["Search"]["value"]
            text += "\nTime of search: " + str(time_stamp_conversion(i["string_map_data"]["Time"]["timestamp"])) + "\n\n"
        return text
    
    def saved_collections():
        text = "Your saved collections and what is in them"
        for i in data["saved_saved_collections"]:
            if "title" in i:
                text += "\n\n\n\nCollection: " + i["string_map_data"]["Name"]["value"]
                text += "\nTime of creation: " + str(time_stamp_conversion(i["string_map_data"]["Creation Time"]["timestamp"])) + "\n\n"
            else:
                text += "Username: " + i["string_map_data"]["Name"]["value"]
                text += "\nTime of addition: " + str(time_stamp_conversion(i["string_map_data"]["Added Time"]["timestamp"]))
                text += "\nLink: " + i["string_map_data"]["Name"]["href"] + "\n\n"
        return text

    def saved_posts():
        text = "Posts you've saved\n\n"
        for i in data["saved_saved_media"]:
            text += "Username: " + i["title"]
            text += "\nTime of saving: " + str(time_stamp_conversion(i["string_map_data"]["Saved on"]["timestamp"]))
            text += "\nLink: " + i["string_map_data"]["Saved on"]["href"] + "\n\n"
        return text

    def emoji_sliders():
        text ="Emoji slider stickers you've interacted with on stories\n\n"
        for i in data["story_activities_emoji_sliders"]:
            text += "Username: " + i["title"]
            text += "\nValue(0-100): " + i["string_list_data"][0]["value"]
            text += "\nTime of interaction: " + str(time_stamp_conversion(i["string_list_data"][0]["timestamp"])) + "\n\n"
        return text

    def polls():
        text = "Poll stickers you've interacted with\n\n"
        for i in data["story_activities_polls"]:
            text += "Username: " + i["title"]
            text += "\nValue: " + i["string_list_data"][0]["value"]
            text += "\nTime of interaction: " + str(time_stamp_conversion(i["string_list_data"][0]["timestamp"])) + "\n\n"
        return text

    def questions():
        text = "Question stickers you've interacted with\n\n"
        for i in data["story_activities_questions"]:
            text += "Username: " + i["title"]
            if i["string_list_data"][0]["value"] != "":
                text += "\nValue: " + i["string_list_data"][0]["value"]
            text += "\nTime of interaction: " + str(time_stamp_conversion(i["string_list_data"][0]["timestamp"])) + "\n\n"
        return text

    def quizzes():
        text = "Quiz stickers you've interacted with\n\n"
        for i in data["story_activities_quizzes"]:
            text += "Username: " + i["title"]
            if i["string_list_data"][0]["value"] != "":
                text += "\nValue: " + i["string_list_data"][0]["value"]
            text += "\nTime of interaction: " + str(time_stamp_conversion(i["string_list_data"][0]["timestamp"])) + "\n\n"
        return text

    def your_topics():
        text = "A collection of topics determined by your activity on Instagram that is used to create recommendations for you in different areas of Instagram, such as Reels, feed recommendations and Shopping\n\n"
        for i in data["topics_your_topics"]:
            text += i["string_map_data"]["Name"]["value"] + "\n"
        return text
        

    def story_likes():
        text = "Stories you've liked\n\n"
        for i in data["story_activities_story_likes"]:
            text += "Username: " + i["title"]
            if i["string_list_data"][0]["value"] != "":
                text += "\nValue: " + i["string_list_data"][0]["value"]
            text += "\nTime of interaction: " + str(time_stamp_conversion(i["string_list_data"][0]["timestamp"])) + "\n\n"
        return text
 
    function_map = {
        "accounts_you're_not_interested_in.json": accounts_you_re_not_interested_in,
        "ads_viewed.json": ads_viewed,
        "posts_viewed.json": posts_viewed,
        "suggested_accounts_viewed.json": suggested_accounts_viewed,
        "videos_watched.json": videos_watched,
        "autofill_information.json": autofill_information,
        "post_comments.json": post_comments,
        "reels_comments.json": reels_comments,
        "synced_contacts.json": synced_contacts,
        "camera_information.json": empty_folder,
        "devices.json": devices,
        "use_of_wallets_across_accounts.json": use_of_wallets_across_accounts,
        "accounts_you've_favorited.json": accounts_you_ve_favorited,
        "blocked_accounts.json": blocked_accounts,
        "follow_requests_you've_received.json": follow_requests_you_ve_received,
        "followers_1.json": followers_1,
        "following.json": following,
        "hide_story_from.json": hide_story_from,
        "pending_follow_requests.json": pending_follow_requests,
        "recent_follow_requests.json": recent_follow_requests,
        "recently_unfollowed_accounts.json": recently_unfollowed_accounts,
        "removed_suggestions.json": removed_suggestions,
        "account_based_in.json": account_based_in,
        "ads_interests.json": ads_interests,
        "advertisers_using_your_activity_or_information.json": advertisers_using_your_activity_or_information,
        "liked_comments.json": liked_comments,
        "liked_posts.json": liked_posts,
        "account_privacy_changes.json": account_privacy_changes,
        "last_known_location.json": last_known_location,
        "login_activity.json": login_activity,
        "logout_activity.json": logout_activity,
        "password_change_activity.json": password_change_activity,
        "signup_information.json": signup_information,
        "comments_allowed_from.json": comments_allowed_from,
        "use_cross_app_messaging.json": use_cross_app_messaging,
        "eligibility.json": eligibility,
        "account_information.json": account_information,
        "linked_meta_accounts.json": linked_meta_accounts,
        "personal_information.json": personal_information,
        "profile_changes.json": profile_changes,
        "notification_of_privacy_policy_updates.json": notification_of_privacy_policy_updates,
        "account_searches.json": account_searches,
        "saved_collections.json": saved_collections,
        "saved_posts.json": saved_posts,
        "emoji_sliders.json": emoji_sliders,
        "polls.json": polls,
        "questions.json": questions,
        "quizzes.json": quizzes,
        "story_likes.json": story_likes,
        "your_topics.json": your_topics
        
        
    }
    file_path_list = file_path.split("/")


    if file_path_list[-1] in function_map:
        return [file_path_list[-1][:-5].replace("_", " "), function_map[file_path_list[-1]]()]
    else:
        return [file_path_list[-1][:-5].replace("_", " "), empty_folder()]
