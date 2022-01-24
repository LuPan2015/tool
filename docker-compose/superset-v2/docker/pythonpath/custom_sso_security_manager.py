import logging
from superset.security import SupersetSecurityManager

class CustomSsoSecurityManager(SupersetSecurityManager):

    def oauth_user_info(self, provider, response=None):
        logging.debug("Oauth2 provider: {0}.".format(provider))
        if provider == 'oauth2_generic':
            # As example, this line request a GET to base_url + '/' + userDetails with Bearer  Authentication,
    # and expects that authorization server checks the token, and response with user details
            me = self.appbuilder.sm.oauth_remotes[provider].get('userInfo').json()
            logging.debug("user_data: {0}".format(me))
            return { 'name' : me['username'], 'email' : me['email'], 'id' : me['userid'], 'username' : me['username'], 'first_name':'', 'last_name':''}
    ...