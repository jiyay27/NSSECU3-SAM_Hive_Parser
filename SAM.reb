Description: Extracts user account details from the SAM hive
Author: John Joseph Donato
Version: 1
Id: 577487c9-332d-413a-99c2-2667ab10ee89
Keys:
    -
        Description: User RIDs and Details
        HiveType: SAM
        Category: User Information
        KeyPath: SAM\Domains\Account\Users
        Recursive: false
        Comment: Lists all user accounts and their RIDs
    -
        Description: Usernames and Corresponding RIDs
        HiveType: SAM
        Category: User Information
        KeyPath: SAM\Domains\Account\Users\Names
        Recursive: true
        Comment: Maps usernames to RIDs
    -
        Description: Last Logon Timestamp
        HiveType: SAM
        Category: User Activity
        KeyPath: SAM\Domains\Account\Users\{RID}
        ValueName: LastLogon
        Recursive: false
        Comment: Shows the last login time for each user (stored as FILETIME)
    -
        Description: Last Password Change
        HiveType: SAM
        Category: User Activity
        KeyPath: SAM\Domains\Account\Users\{RID}
        ValueName: PwdLastSet
        Recursive: false
        Comment: Indicates when the password was last changed (stored as FILETIME)
    -
        Description: Password Hashes (LM & NT)
        HiveType: SAM
        Category: Security
        KeyPath: SAM\Domains\Account\Users\{RID}
        ValueName: V
        Recursive: false
        Comment: Extracts LM & NT hashes (encrypted in 'V' value, offsets required for decryption)
    -
        Description: Account Disabled Status
        HiveType: SAM
        Category: Security
        KeyPath: SAM\Domains\Account\Users\{RID}
        ValueName: AccountDisabled
        Recursive: false
        Comment: Checks if the account is disabled (0x01 = Disabled, 0x00 = Active)
    -
        Description: Failed Logon Count
        HiveType: SAM
        Category: Security
        KeyPath: SAM\Domains\Account\Users\{RID}
        ValueName: FailedLogonCount
        Recursive: false
        Comment: Number of failed login attempts
