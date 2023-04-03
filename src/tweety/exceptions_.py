import traceback

TWITTER_ERRORS = {
    "DefaultApiError": 0,
    "InvalidCoordinates": 3,
    "InvalidGranularity": 4,
    "InvalidAccuracy": 5,
    "NoDataForPoint": 6,
    "NoDataForPointRadius": 7,
    "InvalidId": 8,
    "InvalidMaxResults": 9,
    "RockdoveError": 10,
    "InvalidIp": 11,
    "MustProvideCoordinatesIpQueryOrAttributes": 12,
    "NoLocationForIp": 13,
    "OverlimitAddressBookApi": 14,
    "AddressBookDarkmoded": 15,
    "AddressBookPermissionsError": 16,
    "AddressBookLookupNotFound": 17,
    "TooManyTerms": 18,
    "RetweetDarkmoded": 19,
    "NoScreenNameProvided": 20,
    "ContributorsNotEnabled": 21,
    "NotAuthorizedToViewUser": 22,
    "BulkLookupDarkmoded": 23,
    "UnsupportedProfileImageSize": 24,
    "MissingQuery": 25,
    "AutocompleteMustBeTrueOrFalse": 26,
    "AccountLocked": 27,
    "GenericDarkmode": 28,
    "TimeOut": 29,
    "WoeidDataUnavailable": 30,
    "InvalidTimescale": 31,
    "InvalidCredentials": 32,
    "OverLimit": 33,
    "GenericNotFound": 34,
    "TrendDataUnavailable": 35,
    "CantReportYourselfAsSpam": 36,
    "GenericAccessDenied": 37,
    "MissingParameter": 38,
    "InvalidCreationToken": 39,
    "RockdoveInvalidArgumentError": 41,
    "InvalidAttribute": 42,
    "AttributeAccessDenied": 43,
    "InvalidParameter": 44,
    "InvalidPlaceJson": 46,
    "InvalidRequestUrl": 47,
    "TimeoutRequestRainbird": 48,
    "NoFollowRequest": 49,
    "GenericUserNotFound": 50,
    "PromotedContentOfflineError": 51,
    "PromotedSearchNoQuery": 52,
    "BasicAuthDisabled": 53,
    "CassowaryError": 54,
    "ResourceNotFound": 55,
    "InvalidEmailAddress": 56,
    "PasswordResetPermissionsError": 57,
    "PasswordResetExpiredToken": 58,
    "PasswordResetInvalidHash": 59,
    "PasswordResetMismatchedEntries": 60,
    "ClientNotPermitted": 61,
    "CustomSaveErrors": 62,
    "OtherUserSuspended": 63,
    "CurrentUserSuspended": 64,
    "StrictMustBeTrueOrFalse": 65,
    "RequireActivityMustBeTrueOrFalse": 66,
    "BackendServiceUnavailable": 67,
    "EndpointDeprecated": 68,
    "TalonUrlMalware": 69,
    "InvalidPromotedContentLogEvent": 70,
    "EmailDeliveryError": 71,
    "ApplicationNotFound": 72,
    "ApplicationNotDeleted": 73,
    "ApplicationDomainNotRevoked": 74,
    "ApplicationKeysNotReset": 75,
    "ApplicationImageNotProcessed": 76,
    "ApplicationNoManageRight": 77,
    "ApplicationNoAdminRight": 78,
    "InvalidTrimPlace": 79,
    "CurationDarkmoded": 80,
    "ContributorsAccessLevelNotValid": 81,
    "ContributorsTargetUserNotSpecified": 82,
    "ContributorsTargetUserNotValid": 83,
    "TalonUrlUnrenderable": 84,
    "ValidationFailure": 85,
    "WrongHttpMethod": 86,
    "ClientNotPrivileged": 87,
    "RateLimitExceeded": 88,
    "BadOauthToken": 89,
    "ContributionNotPermitted": 90,
    "InvalidUtf8": 91,
    "SslRequired": 92,
    "DmAccessRequired": 93,
    "PageIsForbidden": 94,
    "InvalidLanguage": 95,
    "InvalidIds": 96,
    "EndpointFeatureDeprecated": 97,
    "FlagPossiblySensitiveScribeError": 98,
    "AuthenticityTokenError": 99,
    "GenericThriftException": 100,
    "InvalidReverseAuthCredentials": 101,
    "DarkmodedFeature": 102,
    "TrendsAvailableTransientException": 103,
    "ListAdminRightsError": 104,
    "MaximumMembersExceeded": 105,
    "AddBlockedUserError": 106,
    "NoTargetUser": 107,
    "TargetUserNotFound": 108,
    "TargetUserNotRelatedToList": 109,
    "ListNotAMemberError": 110,
    "TargetUserSuspended": 111,
    "InsufficientListParameters": 112,
    "InsufficientTargetUserParameters": 113,
    "InvalidCurrentPassword": 114,
    "ListUnauthorizedSubscriptionError": 115,
    "PasswordSmsResetPwSeedNotExist": 116,
    "PasswordSmsResetOptOut": 117,
    "ArgumentTooLarge": 118,
    "NarrowcastNotSupported": 119,
    "AccountUpdateFailure": 120,
    "InvalidHexColor": 121,
    "UpdateProfileColorsError": 122,
    "ImageUpdateError": 123,
    "AttributeUpdateError": 124,
    "GeolocationError": 125,
    "LoggedOut": 126,
    "ArchiveDeprecated": 127,
    "LocationUpdateFailure": 128,
    "EmailRateLimitExceeded": 129,
    "OverCapacity": 130,
    "InternalError": 131,
    "UnusedBackgroundUploadError": 132,
    "NoSelectedBackgroundError": 133,
    "TooManyDevices": 134,
    "OauthTimestampException": 135,
    "BlockedUserError": 136,
    "PushForbidden": 137,
    "FollowingInformationUnavailable": 138,
    "DuplicateFavorite": 139,
    "FollowingStatusUnauthorized": 140,
    "InactiveUser": 141,
    "ProtectedStatusFavoriteError": 142,
    "FavoriteRateLimitExceeded": 143,
    "StatusNotFound": 144,
    "RecordInvalid": 145,
    "OtherUserNotBlocked": 146,
    "SelfBlockError": 147,
    "UnsupportedDevice": 148,
    "InvalidEnabledFor": 149,
    "DirectMessageOtherUserNotFollowing": 150,
    "MessageSendError": 151,
    "DirectMessageDestroyPermissionsError": 152,
    "DirectMessageDeleteError": 153,
    "DirectMessageNotFound": 154,
    "MessageSendUnknownError": 155,
    "DowntimeAlert": 156,
    "VerifiedDeviceNotFound": 157,
    "SelfFollowError": 158,
    "GenericSuspended": 159,
    "DuplicateFollowRequest": 160,
    "FollowRateLimitExceeded": 161,
    "FollowBlockedUserError": 162,
    "IndeterminateSource": 163,
    "TargetUserNotSpecified": 164,
    "MultipleMissingParameters": 165,
    "MultipleUserNotFound": 166,
    "FollowError": 167,
    "StatusNotFoundForbidden": 168,
    "StatusRelatedResultsForbidden": 169,
    "ForbiddenMissingParameter": 170,
    "SearchDeletionError": 171,
    "SearchCreationError": 172,
    "ConfirmEmailExpiredCode": 173,
    "ConfirmEmailInvalidCode": 174,
    "ConfirmEmailInvalidStateChange": 175,
    "ConfirmEmailAlreadyConfirmed": 176,
    "ConfirmEmailSuccessChanged": 177,
    "ConfirmEmailSuccessNew": 178,
    "StatusViewForbidden": 179,
    "GenericEndpointOffline": 180,
    "TimeParameterOrderError": 181,
    "ParameterDeprecated": 182,
    "StatusActionPermissionError": 183,
    "StatusUpdateError": 184,
    "OverStatusUpdateLimit": 185,
    "StatusTooLongError": 186,
    "DuplicateStatusError": 187,
    "StatusMalwareError": 188,
    "StatusCreationError": 189,
    "UnknownInterpreterError": 190,
    "OverPhotoLimit": 191,
    "OverMediaEntitiesPerUpdateLimit": 192,
    "MediaTooLarge": 193,
    "StatusUpdateForbidden": 194,
    "InvalidRequestUrlForbidden": 195,
    "TimelineAuthorizationRequired": 196,
    "CategoryNotFound": 197,
    "ContactLoadError": 198,
    "IdsOfContactsError": 199,
    "GenericForbidden": 200,
    "GetRequired": 201,
    "InternalApplicationAuthenticationDenied": 202,
    "DeviceError": 203,
    "DestinationError": 204,
    "SpamRateLimitExceeded": 205,
    "InvalidDeviceRelationship": 206,
    "AlreadyActivated": 207,
    "FormatNotSupported": 208,
    "DirectMessageMustFollowFirst": 209,
    "TokenLimitExceeded": 210,
    "InvalidBrandBanner": 211,
    "ProfileBannerUploadsDisabled": 212,
    "ProcessingInProgress": 213,
    "GenericBadRequest": 214,
    "BadAuthenticationData": 215,
    "ShareViaEmailRateLimitExceeded": 216,
    "ProtectedStatusShareViaEmailError": 217,
    "RestrictedAccessShareViaEmailError": 218,
    "ShareViaEmailIpRateLimitExceeded": 219,
    "RestrictedAuthToken": 220,
    "CursorInvalid": 221,
    "TieredActionSignupSpammer": 222,
    "EmailTweetSendingError": 223,
    "MissingEmailAddress": 224,
    "TieredActionFollowSpammer": 225,
    "TieredActionTweetSpammer": 226,
    "TieredActionFollowCreeper": 227,
    "TieredActionTweetCreeper": 228,
    "AmbiguousCredentials": 229,
    "UserSleeping": 230,
    "RequiresLoginVerification": 231,
    "CannotEnableLoginVerificationPhone": 232,
    "CannotEnableLoginVerificationAlreadyEnabled": 233,
    "CannotEnableLoginVerificationUnconfirmedEmail": 234,
    "ExpiredLoginVerificationRequest": 235,
    "IncorrectChallengeResponse": 236,
    "MissingLoginVerificationRequest": 237,
    "NewPasswordWeak": 238,
    "BadGuestToken": 239,
    "TieredActionSignupSpammerPhoneVerify": 240,
    "RejectedLoginVerificationRequest": 241,
    "DeactivatedUser": 242,
    "OverLimitLogin": 243,
    "ForcePasswordReset": 244,
    "OverLimitLoginVerificationStart": 245,
    "OverLimitLoginVerificationAttempt": 246,
    "CannotEnableLoginVerificationPush": 247,
    "LoginVerificationAlreadyEnabled": 248,
    "CloudIpRestricted": 249,
    "UserMustBeAlcoholAgeScreened": 250,
    "EndpointRetired": 251,
    "DmSpamTimeout": 252,
    "NotYetApprovedLoginVerification": 253,
    "OfflineCodeSync": 254,
    "RequiresTemporaryPassword": 255,
    "CannotFollowFromCountry": 256,
    "BadDeviceToken": 257,
    "AppsCreateRequiresConfirmedEmail": 258,
    "AppsCreateRequiresVerifiedPhone": 259,
    "AppsCreateRejectedForAbuse": 260,
    "AppInReadOnlyMode": 261,
    "CurrentUserNeedsPhoneVerification": 262,
    "TieredActionChallengeCaptcha": 263,
    "TargetUserNotFollowing": 264,
    "TargetUserNotFavoriteFollowing": 265,
    "FailureSendingLoginVerificationRequest": 266,
    "InvalidCredentialsOneFactorEligible": 267,
    "MissingOneFactorLoginVerificationParams": 268,
    "UserIsNotSdkUser": 269,
    "AppsUpdateSettingsRequiresVerifiedPhone": 270,
    "SelfMuteError": 271,
    "NotMutingTargetUser": 272,
    "ScheduledInPast": 273,
    "ScheduledTooFarInFuture": 274,
    "TooLateToEdit": 275,
    "ScheduleInvalid": 276,
    "DirectMessageRecipientDoesNotFollowSenderWithUnverifiedPhoneNumber": 277,
    "DirectMessageUserNotInConversation": 278,
    "DirectMessageConversationNotFound": 279,
    "DirectMessageTooManyParticipants": 280,
    "DirectMessageTooFewParticipants": 281,
    "DirectMessageRecipientBlocksSender": 282,
    "TieredActionFavoriteSpammer": 283,
    "DeviceRegistrationGeneralError": 284,
    "DeviceAlreadyRegistered": 285,
    "DeviceOperatorUnsupported": 286,
    "UserAlreadyHasVerifiedPhone": 287,
    "CannotReuseCurrentPassword": 288,
    "DevicePinInvalid": 289,
    "DevicePinRequired": 290,
    "UnexpectedDeviceProvided": 291,
    "TieredActionConversationSpammer": 292,
    "SmsVerifyGeneralError": 293,
    "SmsVerifyInvalidPin": 294,
    "SmsVerifyRateLimitExceeded": 295,
    "DtabOverrideDarkmoded": 296,
    "DirectMessageCannotHaveBothTweetAndMedia": 297,
    "DirectMessageTweetNotFound": 298,
    "DeviceRegistrationRateExceeded": 299,
    "DeviceRegistrationInvalidInput": 300,
    "DeviceRegistrationPending": 301,
    "DeviceRegistrationOperationFailed": 302,
    "DeviceRegistrationPhoneNormalizationFailed": 303,
    "DeviceRegistrationPhoneCountryDetectionFailed": 304,
    "CannotIdentifyByEmail": 305,
    "TieredActionAccessTokenGrantSpam": 306,
    "TieredActionAccessTokenRevokeSpam": 307,
    "NoSmsVerifyExists": 308,
    "DeviceNotVerified": 309,
    "ExpiredPin": 310,
    "DirectMessageDuplicate": 311,
    "LocationNameMustBeSpecified": 312,
    "EULANotAccepted": 313,
    "VideoTranscodingError": 314,
    "ClientCaptchaRequired": 315,
    "CannotContributeToYourself": 316,
    "AccountHasTooManyContributors": 317,
    "AccountHasTooManyContributees": 318,
    "CannotChangePassword": 319,
    "ContributorsAccessLevelInsufficient": 320,
    "DirectMessageConversationNameTooLong": 321,
    "DirectMessageGenericUserCouldNotBeAdded": 322,
    "AnimatedGifMultipleImages": 323,
    "InvalidMediaId": 324,
    "MediaNotFound": 325,
    "AccessDeniedByBouncer": 326,
    "AlreadyRetweeted": 327,
    "InvalidRetweetForStatus": 328,
    "NonsupportingClientRequiresLoginVerification": 329,
    "ContributorsGenericUserCouldNotBeAdded": 330,
    "MobileSettingsUserNotFound": 331,
    "MobileSettingsTemplateNotFound": 332,
    "MobileSettingsFileNotFound": 333,
    "MobileSettingsUnsupportedTransport": 334,
    "MobileSettingsSettingNotFound": 335,
    "MobileSettingsInvalidValueFound": 336,
    "MobileSettingsSettingObjectNotFound": 337,
    "MobileSettingsEnabledForMissing": 338,
    "MobileSettingsNoDevicesFound": 339,
    "MobileSettingsNoIncomingPushSettings": 340,
    "MobileSettingsNoIncomingSmsSettings": 341,
    "MobileSettingsIncorrectApplicationId": 342,
    "MobileSettingsNoIncomingSettings": 343,
    "UserActionRateLimitExceeded": 344,
    "OneFactorMethodIsNotSupported": 345,
    "UserIsNotOneFactorEligible": 346,
    "InvalidRequestToken": 347,
    "ClientApplicationNotPermitted": 348,
    "DirectMessageCannotDmOtherUser": 349,
    "OauthException": 350,
    "MobileSettingsCouldNotUpdateSleep": 351,
    "ParameterLimitExceeded": 352,
    "DeniedByApiCsrfProtection": 353,
    "DirectMessageTooLongError": 354,
    "GenericConflict": 355,
    "GenericValidationFailure": 356,
    "RequiredFieldMissing": 357,
    "JsonProcessingError": 358,
    "ValueTooLarge": 359,
    "ValueTooSmall": 360,
    "ValueCannotBeEmpty": 361,
    "TimeNotFuture": 362,
    "InvalidCountryCodes": 363,
    "InvalidTimeGranularity": 364,
    "InvalidUUID": 365,
    "InvalidValues": 366,
    "SizeOutOfRange": 367,
    "TimeNotPast": 368,
    "InvalidJsonSyntax": 369,
    "DigitsCannotReuseCurrentEmail": 370,
    "MentionLimitInTweetExceeded": 371,
    "UrlLimitInTweetExceeded": 372,
    "HashtagLimitInTweetExceeded": 373,
    "ExpiredQrCode": 374,
    "InvalidQrCode": 375,
    "MissingCredentials": 376,
    "TokenRetrievalException": 377,
    "TokenMissing": 378,
    "DataminrUserNotLinked": 379,
    "ABLiveSyncIsDisabled": 380,
    "SoftUserCreationSpamDenied": 381,
    "SoftUserActionSpamDenied": 382,
    "CashtagLimitInTweetExceeded": 383,
    "HashtagLengthLimitInTweetExceeded": 384,
    "InReplyToTweetNotFound": 385,
    "AttachmentTypesLimitInTweetExceeded": 386,
    "NotEnoughFollowers": 387,
    "FeatureAccessLimited": 388,
    "DirectMessagesSenderBlocksRecipient": 389,
    "SearchRecordingNotFound": 390,
    "MaximumSearchRecordingsExceeded": 391,
    "SessionNotFound": 392,
    "SessionModificationNotAuthorized": 393,
    "SessionModificationFailed": 394,
    "VoiceVerifyRateLimitExceeded": 395,
    "BlockUserFailed": 396,
    "InvalidMetricsJson": 397,
    "OnboardingFlowFailure": 398,
    "OnboardingFlowRetriableFailure": 399,
    "NoTwoFactorAuthMethodFound": 400,
    "MomentCapsuleAccessError": 401,
    "CannotEnrollLoginVerificationNotYetEnabled": 402,
    "IneligibleFor2faAfterModification": 403,
    "CookiesRequired": 404,
    "DuplicateBookmark": 405,
    "ProtectedTweetBookmarkError": 406,
    "DirectMessageInactiveDevice": 407,
    "InvalidUrl": 408,
    "BirthdateRequired": 409,
    "PasswordVerificationRequired": 410,
    "DirectMessageSenderInSecretDmsDisabledCountry": 411,
    "DirectMessageRecipientInSecretDmsDisabledCountry": 412,
    "DirectMessageSenderDeviceIsNotActiveForSecretDms": 413,
    "DirectMessageRecipientDeviceIsNotActiveForSecretDms": 414,
    "CallbackUrlLocked": 415,
    "InvalidOrSuspendedApp": 416,
    "InvalidDesktopCallback": 417,
    "DirectMessageSenderIsNotRegisteredForSecretDms": 418,
    "DirectMessageRecipientIsNotRegisteredForSecretDms": 419,
    "ReservedErrorCode": 420,
    "TweetIsBounced": 421,
    "TweetIsBounceDeleted": 422,
    "InvalidHeaders": 423,
    "MomentUnavailableForNewsCamera": 424,
    "TweetEngagementsLimited": 425,
    "InvalidRequestIpv6Token": 426,
    "IpResolverNotAvailable": 427,
    "ValidIpv6TokenRequired": 428,
    "HarmfulLink": 429,
    "ConversationControlNotAllowed": 430,
    "ConversationControlNotSupported": 431,
    "ConversationControlNotAuthorized": 432,
    "ConversationControlReplyRestricted": 433,
    "NotMutingTargetList": 434,
    "ConversationControlInvalidParameter": 435,
    "PassswordRequiredForEmailUpdate": 436,
    "NewPasswordShort": 437,
    "NewPasswordLong": 438,
    "NudgeReceived": 439,
    "CommunityUserNotAuthorized": 440,
    "CommunityNotFound": 441,
    "CommunityRetweetNotAllowed": 442,
    "CommunityInvalidParams": 443,
    "CommunityReplyTweetNotAllowed": 444,
    "RestrictedSession": 445,
    "TokenSecurityLevelAgreementPolicyFailure": 446,
    "SuperFollowsCreateNotAuthorized": 447,
    "SuperFollowsInvalidParams": 448,
    "TOOMomentsList": 449,
    "CommunityProtectedUserCannotTweet": 450,
    "ExclusiveTweetEngagementNotAllowed": 451,
    "SteamCreationException": 452,
    "V11Restricted": 453,
    "SteamGetException": 454,
    "TrustedFriendsInvalidParams": 455,
    "TrustedFriendsRetweetNotAllowed": 456
}


class UserNotFound(Exception):
    """Exception raised when user isn't found.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class GuestTokenNotFound(Exception):
    """
    Exception Raised when the guest token wasn't found after specific number of retires

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class InvalidTweetIdentifier(Exception):
    """
        Exception Raised when the tweet identifier is invalid

        Attributes:
            message -- explanation of the error
    """

    def __init__(self, message="The Identifier provided of the tweet is either invalid or the tweet is private"):
        self.message = message
        super().__init__(self.message)


class ProxyParseError(Exception):
    """
    Exception Raised when an error occurs while parsing the provided proxy

    Attributes:
        message -- explanation of the error
    """

    def __init__(self,message="Error while parsing the Proxy, please make sure you are passing the right formatted proxy"):
        self.message = message
        super().__init__(self.message)


class UserProtected(Exception):
    """
    Exception Raised when an error occurs when the queried User isn't available / Protected

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class UnknownError(Exception):
    """
        Exception Raised when an unknown error occurs

        Attributes:
            message -- explanation of the error
        """

    def __init__(self, message):
        if not isinstance(message, UserProtected) or not isinstance(message, UserNotFound):
            error = traceback.format_exc().splitlines()[-1]
            self.message = error
            super().__init__(self.message)
