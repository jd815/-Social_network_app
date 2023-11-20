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
        
    def events_interactions():
        text = "The number of times you've recently visited the events section on Facebook\n\n"
        for i in data["events_interactions_v2"]:
            text += "Value:" + i["entries"][0]["data"]["value"]
            text += "\nDate of last visit: " + str(time_stamp_conversion(i["entries"][0]["timestamp"])) + "\n\n\n"
        return text

    def group_interactions():
        text = "The number of times you've interacted with groups on Facebook\n\n"
        for i in data["group_interactions_v2"][0]["entries"]:
            text += "Name: " + i["data"]["name"]
            text += "\n" + i["data"]["value"]
            text += "\nLink to group: " + i["data"]["uri"] + "\n\n\n"
        return text

    def people_and_friends():
        text = "People and friends you've interacted with, including comments and reactions not messages\n\n"
        for i in data["people_interactions_v2"][0]["entries"]:
            text += "Name: " + i["data"]["name"]
            text += "\nLink to user: " + i["data"]["uri"]
            text += "\nDate of last interaction: " + str(time_stamp_conversion(i["timestamp"])) + "\n\n\n"
        return text

    def advertisers_using_your_activity_or_information():
        text = """Advertisers using your activity or information\n
        Has data file custom audience: Indicates whether the advertiser has created a custom audience based on a data file that includes your information, such as your email address or phone number.
        Has remarketing custom audience: Indicates whether the advertiser has created a custom audience for remarketing to you, based on your past interactions with the advertiser's website or app.
        Has in person store visit: Indicates whether the advertiser has created a custom audience based on your in-person store visits, if you have enabled location services on your Facebook account.\n\n"""
        for i in data["custom_audiences_all_types_v2"]:
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

    #Decided to change the name slightly so that the apostrophe wouldn't be a problem   
    def advertisers_you_interacted_with():
        text = "Advertisors you've interacted with in the past\n Action: Indicates how you interacted with the ad\n\n"
        for i in data["history_v2"]:
            text += "Name of advertisor: " + i["title"]
            text += "\nAction: " + i["action"]
            text += "\nDate of interaction: " + str(time_stamp_conversion(i["timestamp"])) + "\n\n\n"
        return text

    def apps_and_websites():
        text = "Apps and websites you have connected to your Facebook\nCategory: Represents the status of the app or website associated with your Facebook account\n\n"
        for i in data["installed_apps_v2"]:
            text += "Name of app or Website: " + i["name"]
            text += "\nDate of addition: " + str(time_stamp_conversion(i["added_timestamp"]))
            text += "\nCategory: " + i["category"]
            text += "\nDate of removal: " + str(time_stamp_conversion(i["removed_timestamp"])) + "\n\n\n"

        return text

    def posts_from_apps_and_websites():
        text = "Posts from the apps you've given permission to post on your behalf\n\n"
        for i in data["app_posts_v2"]:
            text += "Title: " + i["title"]
            text += "\nDate of post: " + str(time_stamp_conversion(i["timestamp"]))
            text += "\nName of app: " + i["attachments"][0]["data"][0]["external_context"]["name"]
            text += "\nLink to app: " + i["attachments"][0]["data"][0]["external_context"]["url"] + "\n\n\n"
        return text

    def your_apps():
        text = "Apps you have created\n\n"
        for i in data["admined_apps_v2"]:
            text += "Name: " + i["name"]
            text += "\nDate of addition: " + str(time_stamp_conversion(i["added_timestamp"])) + "\n\n\n"
        return text

    def comments():
        text = "Comments you have posted\n\n"
        for i in data["comments_v2"]:
            text += "Title: " + i["title"]
            text += "\nDate of comment: " + str(time_stamp_conversion(i["timestamp"]))
            text += "\nComment: " + i.get("data", [{}])[0].get("comment", {}).get("comment", "") + "\n\n\n"
        return text

    def likes_and_reactions():
        text = "You're likes and reactions\n\n"
        for i in data["reactions_v2"]:
            text += "Title: " + i["title"]
            text += "\nDate of reaction: " + str(time_stamp_conversion(i["timestamp"]))
            text += "\nReation: " + i["data"][0]["reaction"]["reaction"] + "\n\n\n"
        return text

    def event_invitations():
        text = "Events you've been invited to\n\n"
        for i in data["events_invited_v2"]:
            text += "Name: " + i["name"]
            text += "\nStart of event: " + str(time_stamp_conversion(i["start_timestamp"]))
            text += "\nEnd of event: " + str(time_stamp_conversion(i["end_timestamp"])) + "\n\n\n"
        return text

    def your_event_responses():
        text = "Your responses to Events you've been invited to\n\n"
        text +="Going:\n"
        for i in data["event_responses_v2"]["events_joined"]:
            text += "Name: " + i["name"]
            text += "\nStart of event: " + str(time_stamp_conversion(i["start_timestamp"]))
            text += "\nEnd of event: " + str(time_stamp_conversion(i["end_timestamp"])) + "\n\n"

        text += "\n\nInterested:\n"
        for i in data["event_responses_v2"]["events_interested"]:
            text += "Name: " + i["name"]
            text += "\nStart of event: " + str(time_stamp_conversion(i["start_timestamp"]))
            text += "\nEnd of event: " + str(time_stamp_conversion(i["end_timestamp"])) + "\n\n"

        text += "\n\nNot Going:\n"
        for i in data["event_responses_v2"]["events_declined"]:
            text += "Name: " + i["name"]
            text += "\nStart of event: " + str(time_stamp_conversion(i["start_timestamp"]))
            text += "\nEnd of event: " + str(time_stamp_conversion(i["end_timestamp"])) + "\n\n"
        return text

    def accounts_center():
        text = "Linked accounts across different platforms\n\n"
        for i in data["accounts_center_v2"]["linked_accounts"]:
            text += "Platform: " + i["service_name"]
            text += "\nUsername: " + i["username"]
            text += "\nEmail: " + i["email"]
            text += "\nPhone number: " + i["phone_number"]
            text += "\nName: " + i["name"] + "\n\n\n"

        return text

    def instant_games():
        text = "Apps that connected to your account\n\n"
        for i in data["instant_games_played_v2"]:
            text += "Name of app: " + i["name"]
            text += "\nDate added: " + str(time_stamp_conversion(i["added_timestamp"]))
            text += "\nCategory: " + i["category"] + "\n\n\n"
        return text
    def your_locations():
        text = "Your location(s)\n\n"
        for i in data["news_your_locations_v2"]:
            text += i + "\n"
        return text

    def payment_history():
        text = "Payment history\n\n"
        for key, value in data["payments_v2"].items():
            if key == "preferred_currency":
                text += "Preferred currency: " + value + "\n"
            elif key == "payments":
                text += "Payments:\n"
                for payment in value:
                    text += json.dumps(payment, indent=2) + "\n"
        return text

    def controls():
        text = "Actions you've taken to customize what content you see on Facebook\n\n"
        for i in data["controls"]:
            text += "Name of action: " + i["name"]
            text += "\nDescription: " + i["description"]
            if len(i["entries"]) > 0:
                text += "\nEntries: "
                for entry in i["entries"]:
                    text += "\n" + json.dumps(entry, indent=2)
            text += "\n\n\n"
        return text

    def feed():
        text = "Profiles and Pages you've chosen to see more or less of in your Feed\n\n"
        for i in data["people_and_friends_v2"]:
            text += "Name of action: " + i["name"]
            text += "\nDescription: " + i["description"]
            if len(i["entries"]) > 0:
                text += "\nEntries: "
                for entry in i["entries"]:
                    text += "\n\nName: " + entry["data"]["name"]
                    text += "\nLink to profile: " + entry["data"]["uri"]
                    text += "\nDate of action: " + str(time_stamp_conversion(entry["timestamp"]))
            text += "\n\n\n"
        return text

    def reduce():
        text = "Content you've chosen to reduce, reduce more or not reduce in Feed\n\n"
        for i in data["reduce"]:
            text += "Name of action: " + i["name"]
            text += "\nDescription: " + i["description"]
            if len(i["entries"]) > 0:
                text += "\nEntries: "
                for entry in i["entries"]:
                    text += "\n\nName: " + entry["data"]["name"]
                    text += "\n\nAction: " + entry["data"]["value"]

            text += "\n\n\n"
        return text

    def friend_requests_received():
        text = "Requests from others asking you to be friends on Facebook\n\n"
        for i in data["received_requests_v2"]:
            text += "Name: " + i["name"]
            text += "\nDate of request: " + str(time_stamp_conversion(i["timestamp"])) + "\n\n\n"

        return text

    def friend_requests_sent():
        text = "Requests to others asking them to be friends on Facebook\n\n"
        for i in data["sent_requests_v2"]:
            text += "Name: " + i["name"]
            text += "\nDate of request: " + str(time_stamp_conversion(i["timestamp"])) + "\n\n\n"

        return text

    def friends_you_see_less():
        text = "Friends whose activity you've chosen to see less of on Facebook\n\n"
        for i in data["friends_you_see_less_v2"]:
            for entry in i["entries"]:
                text += "Name: " + entry["data"]["name"]
                text += "\nDate of request: " + str(time_stamp_conversion(entry["timestamp"]))
                text += "\nLink to user: " + entry["data"]["uri"] + "\n\n\n"
        return text

    def friends():
        text = "People you are currently connected to\n\n"
        for i in data["friends_v2"]:
            text += "Name: " + i["name"]
            text += "\nDate of start of friendship: " + str(time_stamp_conversion(i["timestamp"])) + "\n\n\n"
        return text

    def rejected_friend_requests():
        text = "People who's friend request you have rejected\n\n"
        for i in data["rejected_requests_v2"]:
            text += "Name: " + i["name"]
            text += "\nDate of rejection: " + str(time_stamp_conversion(i["timestamp"])) + "\n\n\n"
        return text

    def removed_friends():
        text = "Friends you have removed\n\n"
        for i in data["deleted_friends_v2"]:
            text += "Name: " + i["name"]
            text += "\nDate of removal: " + str(time_stamp_conversion(i["timestamp"])) + "\n\n\n"
        return text

    def who_you_follow():
        text = "People or pages you follow\n\n"
        for i in data["following_v2"]:
            text += "Name: " + i["name"]
            text += "\nDate when you started following: " + str(time_stamp_conversion(i["timestamp"])) + "\n\n\n"
        return text

    def your_comments_in_groups():
        text = "Comments you have made in groups\n\n"
        for i in data["group_comments_v2"]:
            text += "Title: " + i["title"]
            if "data" in i:
                text += "Group name: " + i.get("data", [])[0].get("comment", {}).get("group", "")
                text += "\nComment: " + i.get("data", [])[0].get("comment", {}).get("comment", "")
            text += "\nDate of comment : " + str(time_stamp_conversion(i["timestamp"])) + "\n\n\n"
        return text

    def your_group_membership_activity():
        text = "Dates you joined the groups you belong to\n\n"
        for i in data["groups_joined_v2"]:
            text += "Title: " + i["title"]
            if "data" in i:
                text += "\nName: " + i["data"][0]["name"]
            text += "\nDate when you joined: " + str(time_stamp_conversion(i["timestamp"])) + "\n\n\n"
        return text

    def device_location():
        text = "Information about your device(s)\n\n"
        for i in data["phone_number_location_v2"]:
            text += "Service provider name: " + i["spn"]
            text += "\nCountry code: " + i["country_code"]
        return text

    def primary_location():
        text = "Your primary location\n\n"
        for i in data["primary_location_v2"]["city_region_pairs"]:
            text += "Location: " + i[0] + ", " + i[1]
            text += "\nZipcode: " + data["primary_location_v2"]["zipcode"][0]
        return text

    def primary_public_location():
        text = "Your primary location based on your public information and activity on Facebook\n\n"
        i = data["primary_public_location_v2"]
        text += "City: " + i["city"]
        text += "\nRegion: " + i["region"]
        text += "\nCountry: " + i["country"]
        return text

    def timezone():
        text = "Your timezone: " + data["timezone_v2"]
        return text

    def notification_of_meta_privacy_policy_update():
        text = "Privacy policy updates you've received notifications for\n\n"
        for i in data["notification_meta_privacy_policy_update"]:
            text += "Notification received on: " + str(time_stamp_conversion(i["impression_time"])) + "\n"
            text += "Have you given consent? "
            if i["consent_state"] == 1:
                text += "Yes"
            else:
                text += "No"
            text += "\n\n\n"
        return text

    def notifications():
        text = "Your recent notifications on Facebook\n\n"
        for i in data["notifications_v2"]:
            text += "Timestamp: " + str(time_stamp_conversion(i["timestamp"])) + "\n"
            text += "Unread: "
            if i["unread"]:
                text += "Yes"
            else:
                text += "No"
            text += "\n"
            text += "Notification text: " + i["text"] + "\n"
            text += "Link: " + i["href"] + "\n\n\n"
        return text

    def pokes():
        text = "Pokes you've received on Facebook\nRank: Represents the level of intensity or frequency of the poke\n\n"
        for poke in data["pokes_v2"]:
            text += "Poker: " + poke["poker"] + "\n"
            text += "Date: " + str(time_stamp_conversion(poke["timestamp"])) + "\n"
            text += "Pokee: " + poke["pokee"] + "\n"
            text += "Rank: " + str(poke["rank"]) + "\n\n\n"
        return text

    def ads_interests():
        text = "Interests Facebook has gathered about you to show you relevant ads. Facebook sells you to ads that look for people with these interests.\n\n"
        for i in data["topics_v2"]:
            text += i + "\n"
        return text

    def your_address_books():
        text = "Your Facebook address book\n\n"
        for entry in data["address_book_v2"]["address_book"]:
            text += "Name: " + entry["name"] + "\n"
            for detail in entry["details"]:
                text += "Contact point: " + detail["contact_point"] + "\n"
            text += "Created: " + str(time_stamp_conversion(entry["created_timestamp"])) + "\n"
            text += "Last updated: " + str(time_stamp_conversion(entry["updated_timestamp"])) + "\n\n\n"
        return text

    def pages_and_profiles_you_follow():
        text = "Pages you have followed on Facebook\n\n"
        for page in data["pages_followed_v2"]:
            text += "Name: " + page["data"][0]["name"] + "\n"
            text += "Date followed: " + str(time_stamp_conversion(page["timestamp"])) + "\n\n\n"
        return text

    def pages_and_profiles_you_ve_unfollowed():
        text = "Pages and profiles you've unfollowed on Facebook\n\n"
        for i in data["pages_unfollowed_v2"]:
            text += "Name: " + i["data"][0]["name"]
            text += "\nDate unfollowed: " + str(time_stamp_conversion(i["timestamp"])) + "\n\n\n"
        return text

    def pages_you_ve_liked():
        text = "Pages you have liked on Facebook\n\n"
        for page in data["page_likes_v2"]:
            text += "Name: " + page["name"]
            text += "\nDate of like: " + str(time_stamp_conversion(page["timestamp"])) + "\n"
            text += "Link to page: " + page["url"] + "\n\n\n"
        return text

    def polls_you_voted_on():
        text = "Polls you've voted on:\n\n"
        for poll in data["poll_votes_v2"]:
            text += "Title: " + poll["title"]
            text += "\nDate of poll: " + str(time_stamp_conversion(poll["timestamp"]))
            for option in poll["attachments"][0]["data"][0]["poll"]["options"]:
                if option["voted"]:
                    text += "\nOption: " + option["option"]
            text += "\n\n\n"
        return text

    def language_and_locale():
        # Get selected language
        text = "Your selected language for your Facebook experience is: "
        for i in data["language_and_locale_v2"][0]["children"][0]["entries"]:
            text += i["data"]["value"]
        text += "\n\n"

        # Get locale changes
        text += "Your history of changes to your locale setting:\n"
        for i in data["language_and_locale_v2"][0]["children"][1]["entries"]:
            text += "Locale: " + i["data"]["name"]
            text += "\nTimestamp: " + str(time_stamp_conversion(i["timestamp"])) + "\n\n"

        # Get languages you may know
        text += "\nLanguages you may know as determined by your activity on Facebook: "
        for i in data["language_and_locale_v2"][1]["entries"]:
            text += i["data"]["value"]

        # Get preferred language
        text += "\n\nYour preferred language(s) as determined by your activity on Facebook: "
        for i in data["language_and_locale_v2"][2]["entries"]:
            text += i["data"]["value"]

        return text

    def autofill_information():
        text = "Information Facebook has to autofill entries for you\n\n"
        if len(data["media"]) > 0:
            for i in data["media"]:
                text += i + "\n\n"
            text += "\n"
        for i in data["label_values"]:
            if i["value"] != "":
                text += i["label"] + ": " + i["value"] + "\n\n"
        return text

    def profile_information():
        text = "Your name, birth date, work and education information and places you've lived that you've added to your profile\n\n"        
        if data["profile_v2"]["name"]["full_name"] != "":
            text += "Full Name: " + data["profile_v2"]["name"]["full_name"] + "\n"

        if data["profile_v2"]["name"]["first_name"] != "":
            text += "First Name: " + data["profile_v2"]["name"]["first_name"] + "\n"

        if data["profile_v2"]["name"]["middle_name"] != "":
            text += "Middle Name: " + data["profile_v2"]["name"]["middle_name"] + "\n"

        if data["profile_v2"]["name"]["last_name"] != "":
            text += "Last Name: " + data["profile_v2"]["name"]["last_name"] + "\n"

        if data["profile_v2"]["emails"]["emails"] != []:
            text += "Emails: " + ", ".join(data["profile_v2"]["emails"]["emails"]) + "\n"

        if data["profile_v2"]["emails"]["previous_emails"] != []:
            text += "Previous Emails: " + ", ".join(data["profile_v2"]["emails"]["previous_emails"]) + "\n"

        if data["profile_v2"]["birthday"]["year"] != 0:
            text += "Birthday: " + str(data["profile_v2"]["birthday"]["month"]) + "/" + str(data["profile_v2"]["birthday"]["day"]) + "/" + str(data["profile_v2"]["birthday"]["year"]) + "\n"

        if data["profile_v2"]["gender"]["gender_option"] != "":
            text += "Gender: " + data["profile_v2"]["gender"]["gender_option"] + "\n"

        if data["profile_v2"]["gender"]["pronoun"] != "":
            text += "Pronoun: " + data["profile_v2"]["gender"]["pronoun"] + "\n"

        if data["profile_v2"]["family_members"] != []:
            text += "Family Members:\n"
            for family_member in data["profile_v2"]["family_members"]:
                text += "\tName: " + family_member["name"] + "\n"
                text += "\tRelation: " + family_member["relation"] + "\n"
                text += "\tDate of last interaction: " + str(time_stamp_conversion(family_member["timestamp"])) + "\n\n"

        if data["profile_v2"]["education_experiences"] != []:
            text += "Education Experiences:\n"
            for education_experience in data["profile_v2"]["education_experiences"]:
                text += "\tName: " + education_experience["name"] + "\n"
                text += "\tGraduated: " + str(education_experience["graduated"]) + "\n"
                text += "\tSchool Type: " + education_experience["school_type"] + "\n"
                text += "\tDate of last interaction: " + str(time_stamp_conversion(education_experience["timestamp"])) + "\n\n"

        if data["profile_v2"]["work_experiences"] != []:
            text += "Work Experiences:\n"
            for work_experience in data["profile_v2"]["work_experiences"]:
                text += work_experience + "\n"
            text += "\n\n"

        if data["profile_v2"]["websites"] != []:
            text += "Websites:\n"
            for website in data["profile_v2"]["websites"]:
                text += website + "\n"
            text += "\n\n"

        if data["profile_v2"]["phone_numbers"] != []:
            text += "Phone Numbers:\n"
            for phone_number in data["profile_v2"]["phone_numbers"]:
                text += "\tType: " + phone_number["phone_type"] + "\n"
                text += "\tNumber: " + phone_number["phone_number"] + "\n"
                text += "\tVerified: " + str(phone_number["verified"]) + "\n\n"
        if data["profile_v2"]["registration_timestamp"] != 0:
            text += "Registration Date: " + str(time_stamp_conversion(data["profile_v2"]["registration_timestamp"])) + "\n"

        if data["profile_v2"]["profile_uri"] != "":
            text += "Profile Link: " + data["profile_v2"]["profile_uri"] + "\n"
        return text

    def profile_update_history():
        text = "Updates to your profile\n\n"
        for i in data["profile_updates_v2"]:
            text += str(i["title"])
            text += "\nDate of update: " + str(time_stamp_conversion(i["timestamp"])) + "\n\n\n"
        return text

    def your_saved_items():
        text = "Posts, photos and videos you have saved\n\n"
        for i in data["saves_v2"]:
            text += i["title"]
            text += "\nDate of save: " + str(time_stamp_conversion(i["timestamp"]))
            text += "\nName of item: " + i["attachments"][0]["data"][0]["external_context"]["name"]
            text += "\nSource of item: " + i["attachments"][0]["data"][0]["external_context"]["source"]
            text += "\nLink to item: " + i["attachments"][0]["data"][0]["external_context"]["url"] + "\n\n\n"
        return text

    def your_search_history():
        text = "Your search history on Facebook\n\n"
        for i in data["searches_v2"]:
            text += str(i["title"])
            text += "\nDate of search: " + str(time_stamp_conversion(i["timestamp"]))
            text += "\nSearch query: " + str(i["data"][0]["text"])
            text += "\n\n\n"
        return text

    def account_activity():
        text = "Activity on your account\n\n"
        for i in data["account_activity_v2"]:
            text += "Action: " + i["action"]
            text += "\nDate of action: " + str(time_stamp_conversion(i["timestamp"]))
            text += "\nIp address: " + i["ip_address"]
            text += "\nUsers browser: " + i["user_agent"]
            text += "\nCity: " + i["city"]
            text += "\nRegion: " + i["region"]
            text += "\nCountry: " + i["country"]
            if "site_name" in i:
                text += "\nSite name: " + i["site_name"] + "\n\n"
            else:
                text += "\n\n"            
        return text

    def account_status_changes():
        text = "Changes to the status of your account\n\n"
        for i in data["account_status_changes_v2"]:
            text += "Status: " + i["status"]
            text += "\nDate of change: " + str(time_stamp_conversion(i["timestamp"])) + "\n\n"
        return text

    def email_address_verifications():
        text = "Your verified contacts\n\n"
        for i in data["contact_verifications_v2"]:
            text += "Contact: " + i["contact"]
            text += "\n Date of verification: " + str(time_stamp_conversion(i["verification_time"])) + "\n\n"
        return text

    def ip_address_activity():
        text = "Your used ip addresses\n\n"
        for i in data["used_ip_address_v2"]:
            text += "ip address: " + i["ip"]
            text += "\nAction from that ip address: " + i["action"]
            text += "\nTime of action: " + str(time_stamp_conversion(i["timestamp"]))
            text += "\n Browser used: " + i["user_agent"] + "\n\n\n"
        return text

    def login_protection_data():
        text ="Your location at login\n\n"
        for i in data["login_protection_data_v2"]:
            text += i["name"]
            text += "\nDate of first login from here: " + str(time_stamp_conversion(i["session"]["created_timestamp"]))
            if "updated_timestamp" in i["session"]:
                text += "\nDate of most recent login from here: " + str(time_stamp_conversion(i["session"]["updated_timestamp"]))
            if i["name"][:2] == "IP":
                text += "\n\n"
            else:
                if "ip_address" in i["session"]:
                    text += "\nIP address: " + i["session"]["ip_address"] + "\n\n"
        return text

    def logins_and_logouts():
        text ="Actions(Login, Log out) from different ip addresses\n\n"
        for i in data["account_accesses_v2"]:
            text += "Action: " + i["action"]
            text += "\nDate: " + str(time_stamp_conversion(i["timestamp"]))
            text += "\nSite: " + i["site"]
            if "ip_address" in i:
                text += "\nIP address: " + i["ip_address"]
            text += "\n\n"
        return text

    def mobile_devices():
        text = "Devices you logged on with\n\n"
        for i in data["devices_v2"]:
            text += "Type: " + i["type"]
            text += "\nOperating system: " + i["os"]
        return text

    def record_details():
        text = "Records details of admin events\n\n"
        for i in data["admin_records_v2"]:
            text += "Event: " + i["event"]
            text += "\nDate of event: " + str(time_stamp_conversion(i["session"]["created_timestamp"]))
            if "ip_address" in i["session"]:
                text += "\nIP address: " + i["session"]["ip_address"]
            if "extra_info" in i:
                for key, value in i['extra_info'].items():
                    if value not in ("", None):
                        text += "\n" + key + ": " + value
            text  += "\n\n"
        return text

    def where_you_re_logged_in():
        text = "Your active sessions\n\n"
        for i in data["active_sessions_v2"]:
            text += "IP address: " + i["ip_address"]
            text += "\nDate of start of session: " + str(time_stamp_conversion(i["created_timestamp"]))
            text += "\nBrowser: " + i["user_agent"]
            text += "\nDevice: " + i["device"]
            text += "\nLocation: " + i["location"] + "\n\n"
        return text
            
    def your_facebook_activity_history():
        text = "Your history of when you've accessed Facebook\n\n"
        i = data["last_activity_v2"]["last_activity_time"]
        if "Website" in i:
            text += "Website: "
            for x in i["Website"]["activity_by_day"]:
                text += "\n" + str(time_stamp_conversion(x))
        if "Facebook app" in i:
            text += "\n\nFacebook app: "
            for x in i["Facebook app"]["activity_by_day"]:
                text += "\n" + str(time_stamp_conversion(x))
        if "iPhone" in i:
            text += "\n\niPhone: "
            for x in i["iPhone"]["activity_by_day"]:
                text += "\n" + str(time_stamp_conversion(x))
        return text

    def location():
        text = "Your voting location(s):\n\n"
        text += data["voting_location_v2"]["voting_location"]
        return text
    
    def voting_reminders():
        text = "Your preferences for notifications from Facebook about voting and elections\n\n"
        text += data["voting_reminders_v2"]["voting_reminders"]
        return text
    
    def recently_viewed():
        text = "Items you've recently viewed on Facebook including articles, groups, Stories, Marketplace items, Live videos and more\n\n"
        for i in data["recently_viewed"]:
            text += i["name"] + "\n"
            text += "Description: " + i["description"] + "\n\n"
            if "children" in i.keys():
                for child in i["children"]:
                    text += child["name"] + ": " + child["description"] + "\n\n"
                    if len(child["entries"][0]["data"]) == 1:
                        for entry in child["entries"]:
                            text += entry["data"]["value"] + "\n"
                        text += "\n\n"
                    else:
                        for entry in child["entries"]:
                            text += "name: " + entry["data"]["name"]
                            text += "\nLink to content: " + entry["data"]["uri"]
                            if "watch_time" in entry["data"]:
                                text += "\nTime spent watching: " + entry["data"]["watch_time"]
                            elif "watch_position_seconds" in entry["data"]:
                                text += "\nWhere you stopped: " + entry["data"]["watch_position_seconds"]
                            text += "\nDate of viewing: " + str(time_stamp_conversion(entry["timestamp"]))+"\n\n"
            else:
                for entry in i["entries"]:
                    text += "Name: " + entry["data"]["name"]
                    if "uri" in entry["data"]:
                        text += "\nLink to item: " + entry["data"]["uri"]
                    elif "share" in entry["data"]:
                        text += "\nLink to item: " + entry["data"]["share"]
                    text += "Date of viewing: " + str(time_stamp_conversion(entry["timestamp"])) + "\n\n"
            text += "\n\n\n\n\n"
        return text

    def recently_visited():
        text = "Areas of Facebook you've recently visited including people's profiles, Pages, groups and events\n\n"
        for i in data["visited_things_v2"]:
            text += i["name"] + "\n"
            text += "Description:" + i["description"] + "\n\n"
            for entry in i["entries"]:
                if "value" in entry["data"]:
                    text += entry["data"]["value"] + "\n"
                else:
                    text += "Name: " + entry["data"]["name"]
                    text += "\nDate of visit: " + str(time_stamp_conversion(entry["timestamp"]))
                    text += "\nLink: " + entry["data"]["uri"] + "\n\n"
            text+= "\n\n\n"
        return text

    def your_topics():
        text = "A collection of topics determined by your activity on Facebook that is used to create recommendations for you in different areas of Facebook such as Feed, News and Watch\n\n"
        for i in data["inferred_topics_v2"]:
            text += i + "\n"
        return text


    function_map = {
        "events_interactions.json": events_interactions,
        "group_interactions.json": group_interactions,
        "people_and_friends.json": people_and_friends,
        "advertisers_using_your_activity_or_information.json": advertisers_using_your_activity_or_information,
        "advertisers_you\'ve_interacted_with.json": advertisers_you_interacted_with,
        "apps_and_websites.json": apps_and_websites,
        "posts_from_apps_and_websites.json": posts_from_apps_and_websites,
        "your_apps.json": your_apps,
        #"your_off_facebook-activity.json": your_off_facebook_activity,
        "comments.json": comments,
        "likes_and_reactions.json": likes_and_reactions,
        "event_invitations.json": event_invitations,
        "your_event_responses.json": your_event_responses,
        "accounts_center.json": accounts_center,
        "instant_games.json": instant_games,
        "your_locations.json": your_locations,
        "payment_history.json": payment_history,
        "controls.json": controls,
        "feed.json": feed,
        "reduce.json": reduce,
        "friend_requests_received.json": friend_requests_received,
        "friend_requests_sent.json": friend_requests_sent,
        "friends_you_see_less.json": friends_you_see_less,
        "friends.json": friends,
        "rejected_friend_requests.json": rejected_friend_requests,
        "removed_friends.json": removed_friends,
        "who_you_follow.json": who_you_follow,
        "your_comments_in_groups.json": your_comments_in_groups,
        "your_group_membership_activity.json": your_group_membership_activity,
        "device_location.json": device_location,
        "primary_location.json": primary_location,
        "primary_public_location.json": primary_public_location,
        "timezone.json": timezone,
        "notification_of_meta_privacy_policy_update.json": notification_of_meta_privacy_policy_update,
        "notifications.json": notifications,
        "pokes.json": pokes,
        "ads_interests.json": ads_interests,
        "your_address_books.json": your_address_books,
        "pages_and_profiles_you_follow.json": pages_and_profiles_you_follow,
        "pages_and_profiles_you've_unfollowed.json": pages_and_profiles_you_ve_unfollowed,
        "pages_you've_liked.json": pages_you_ve_liked,
        "polls_you_voted_on.json": polls_you_voted_on,
        "language_and_locale.json": language_and_locale,
        "autofill_information.json": autofill_information,
        "profile_information.json": profile_information,
        "profile_update_history.json": profile_update_history,
        "your_saved_items.json": your_saved_items,
        "your_search_history.json": your_search_history,
        "account_activity.json": account_activity,
        "account_status_changes.json": account_status_changes,
        "email_address_verifications.json": email_address_verifications,
        "ip_address_activity.json": ip_address_activity,
        "login_protection_data.json": login_protection_data,
        "logins_and_logouts.json": logins_and_logouts,
        "record_details.json": record_details,
        "where_you're_logged_in.json": where_you_re_logged_in, 
        "location.json": location,
        "your_facebook_activity_history.json": your_facebook_activity_history,
        "mobile_devices.json": mobile_devices,
        "voting_reminders.json": voting_reminders,
        "recently_viewed.json": recently_viewed,
        "recently_visited.json": recently_visited,
        "your_topics.json": your_topics,
        "browser_cookies.json": empty_folder
    }
    file_path_list = file_path.split("/")
    if file_path_list[-1] in function_map:
        return [file_path_list[-1][:-5].replace("_", " "), function_map[file_path_list[-1]]()]
    else:
        return [file_path_list[-1][:-5].replace("_", " "), empty_folder()]
