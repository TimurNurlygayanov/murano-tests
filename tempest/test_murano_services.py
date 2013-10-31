# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2013 Mirantis, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import testtools

from tempest import exceptions
from tempest.test import attr
from tempest.tests.murano import base

class SanityMuranoTest(base.MuranoTest):

    @attr(type='smoke')
    def test_create_and_delete_AD(self):
        """ Create and delete AD
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to add AD
            4. Send request to remove AD
            5. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        self.environments.append(env)
        resp, sess = self.create_session(env['id'])
        resp, serv = self.create_AD(env['id'], sess['id'])
        resp = self.delete_service(env['id'], sess['id'], serv['id'])
        resp = self.delete_environment(env['id'])
        self.environments.pop(self.environments.index(env))

    @testtools.skip('It is look as a bug')
    @attr(type='negative')
    def test_create_AD_wo_env_id(self):
        """ Try create AD without env_id
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to add AD using wrong env_id
            4. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        self.environments.append(env)
        resp, sess = self.create_session(env['id'])
        self.assertRaises(Exception, self.create_AD,
                          None, sess['id'])
        resp = self.delete_environment(env['id'])
        self.environments.pop(self.environments.index(env))

    @attr(type='negative')
    def test_create_AD_wo_sess_id(self):
        """ Try to create AD without session id
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to add AD using uncorrect session id
            5. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        self.environments.append(env)
        resp, sess = self.create_session(env['id'])
        self.assertRaises(Exception, self.create_AD,
                          env['id'], "")
        resp = self.delete_environment(env['id'])
        self.environments.pop(self.environments.index(env))

    @testtools.skip("It is look like a bug")
    @attr(type='negative')
    def test_delete_AD_wo_env_id(self):
        """ Try to delete AD without environment id
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to add AD
            4. Send request to remove AD using uncorrect environment id
            5. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        self.environments.append(env)
        resp, sess = self.create_session(env['id'])
        resp, serv = self.create_AD(env['id'], sess['id'])
        self.assertRaises(Exception, self.delete_service,
                          None, sess['id'], serv['id'])
        resp = self.delete_environment(env['id'])
        self.environments.pop(self.environments.index(env))

    @attr(type='negative')
    def test_delete_AD_wo_session_id(self):
        """ Try to delete AD without session id
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to add AD
            4. Send request to remove AD using wrong session id
            5. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        self.environments.append(env)
        resp, sess = self.create_session(env['id'])
        resp, serv = self.create_AD(env['id'], sess['id'])
        self.assertRaises(Exception, self.delete_service,
                          env['id'], "", serv['id'])
        resp = self.delete_environment(env['id'])
        self.environments.pop(self.environments.index(env))

    @attr(type='smoke')
    def test_create_and_delete_IIS(self):
        """ Create and delete IIS
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to add IIS
            4. Send request to remove IIS
            5. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        self.environments.append(env)
        resp, sess = self.create_session(env['id'])
        resp, serv = self.create_IIS(env['id'], sess['id'])
        resp = self.delete_service(env['id'], sess['id'], serv['id'])
        resp = self.delete_environment(env['id'])
        self.environments.pop(self.environments.index(env))

    @testtools.skip('It is look as a bug')
    @attr(type='negative')
    def test_create_IIS_wo_env_id(self):
        """ Try to create IIS without env id
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to add IIS using wrong environment id
            4. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        self.environments.append(env)
        resp, sess = self.create_session(env['id'])
        self.assertRaises(Exception, self.create_IIS,
                          None, sess['id'])
        resp = self.delete_environment(env['id'])
        self.environments.pop(self.environments.index(env))

    @attr(type='negative')
    def test_create_IIS_wo_sess_id(self):
        """ Try to create IIS without session id
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to add IIS using wrong session id
            4. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        self.environments.append(env)
        resp, sess = self.create_session(env['id'])
        self.assertRaises(Exception, self.create_IIS,
                          env['id'], "")
        resp = self.delete_environment(env['id'])
        self.environments.pop(self.environments.index(env))

    @testtools.skip("It is look like a bug")
    @attr(type='negative')
    def test_delete_IIS_wo_env_id(self):
        """ Try to delete IIS without env id
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to add IIS
            4. Send request to delete IIS using wrong environment id
            5. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        self.environments.append(env)
        resp, sess = self.create_session(env['id'])
        resp, serv = self.create_IIS(env['id'], sess['id'])
        self.assertRaises(Exception, self.delete_service,
                          None, sess['id'], serv['id'])
        resp = self.delete_environment(env['id'])
        self.environments.pop(self.environments.index(env))

    @attr(type='negative')
    def test_delete_IIS_wo_session_id(self):
        """ Try to delete IIS without session id
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to add IIS
            4. Send request to delete IIS using wrong session id
            5. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        self.environments.append(env)
        resp, sess = self.create_session(env['id'])
        resp, serv = self.create_IIS(env['id'], sess['id'])
        self.assertRaises(Exception, self.delete_service,
                          env['id'], "", serv['id'])
        resp = self.delete_environment(env['id'])
        self.environments.pop(self.environments.index(env))

    @attr(type='smoke')
    def test_create_and_delete_apsnet(self):
        """ Create and delete apsnet
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to add apsnet
            4. Send request to remove apsnet
            5. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        self.environments.append(env)
        resp, sess = self.create_session(env['id'])
        resp, serv = self.create_apsnet(env['id'], sess['id'])
        resp = self.delete_service(env['id'], sess['id'], serv['id'])
        resp = self.delete_environment(env['id'])
        self.environments.pop(self.environments.index(env))

    @testtools.skip('It is look as a bug')
    @attr(type='negative')
    def test_create_apsnet_wo_env_id(self):
        """ Try to create aspnet without env id
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to add aspnet using wrong environment id
            4. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        self.environments.append(env)
        resp, sess = self.create_session(env['id'])
        self.assertRaises(Exception, self.create_apsnet,
                          None, sess['id'])
        resp = self.delete_environment(env['id'])
        self.environments.pop(self.environments.index(env))

    @attr(type='negative')
    def test_create_apsnet_wo_sess_id(self):
        """ Try to create aspnet without session id
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to add aspnet using wrong session id
            4. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        self.environments.append(env)
        resp, sess = self.create_session(env['id'])
        self.assertRaises(Exception, self.create_apsnet,
                          env['id'], "")
        resp = self.delete_environment(env['id'])
        self.environments.pop(self.environments.index(env))

    @testtools.skip("It is look like a bug")
    @attr(type='negative')
    def test_delete_apsnet_wo_env_id(self):
        """ Try to delete aspnet without env id
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to add aspnet
            4. Send request to delete aspnet using wrong environment id
            5. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        self.environments.append(env)
        resp, sess = self.create_session(env['id'])
        resp, serv = self.create_apsnet(env['id'], sess['id'])
        self.assertRaises(Exception, self.delete_service,
                          None, sess['id'], serv['id'])
        resp = self.delete_environment(env['id'])
        self.environments.pop(self.environments.index(env))

    @attr(type='negative')
    def test_delete_apsnet_wo_session_id(self):
        """ Try to delete aspnet without session id
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to add aspnet
            4. Send request to delete aspnet using wrong session id
            5. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        self.environments.append(env)
        resp, sess = self.create_session(env['id'])
        resp, serv = self.create_apsnet(env['id'], sess['id'])
        self.assertRaises(Exception, self.delete_service,
                          env['id'], "", serv['id'])
        resp = self.delete_environment(env['id'])
        self.environments.pop(self.environments.index(env))

    @attr(type='smoke')
    def test_create_and_delete_IIS_farm(self):
        """ Create and delete IIS farm
        Target component: Murano

        Scenario:
            1. Send request to create environment
            2. Send request to create session
            3. Send request to add IIS farm
            4. Send request to remove IIS farm
            5. Send request to delete environment
        """
        resp, env = self.create_environment('test')
        self.environments.append(env)
        resp, sess = self.create_session(env['id'])
        resp, serv = self.create_IIS_farm(env['id'], sess['id'])
        resp = self.delete_service(env['id'], sess['id'], serv['id'])
        resp = self.delete_environment(env['id'])
        self.environments.pop(self.environments.index(env))
