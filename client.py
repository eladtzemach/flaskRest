from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3


class GetClient(Resource):

    def get(self,id):

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM clients WHERE id=?"
        result = cursor.execute(query, (id,))
        # gives the first item found by this filter function.
        # if it doesn't find the user, return None
        row = result.fetchone()
        connection.close()

        if row:
            return {'client': {'id': row[0], 'name': row[1], 'email': row[2], 'phone number': row[3], \
            'address': row[4], 'city': row[5], 'postal code': row[6], 'country': row[7]}}
        else:
            return {'message': 'Client not found.'}, 404


class ModifyClient(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int, required=True)
    parser.add_argument('name', type=str)
    parser.add_argument('email', type=str)
    parser.add_argument('phone', type=str)
    parser.add_argument('address', type=str)
    parser.add_argument('city', type=str)
    parser.add_argument('postalcode', type=str)
    parser.add_argument('country', type=str)

    # have to authenticate before calling POST
    @jwt_required()
    def post(self):

        data = ModifyClient.parser.parse_args()
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM clients WHERE id=?"
        result = cursor.execute(query, (data['id'],))
        row = result.fetchone()

        if row:
            return {'message': "A client with id '{}' already exists.".format(data['id'])}, 400

        client = {'id': data['id'], 'name': data['name'], 'email': data['email'], 'phone': data['phone'], \
                  'street': data['address'], 'city': data['city'], 'postalcode': data['postalcode'], \
                  'country': data['country']}

        query = "INSERT INTO clients VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (client['id'], client['name'], client['email'], client['phone'], client['street'], \
                               client['city'], client['postalcode'], client['country']))
        connection.commit()
        connection.close()
        return client, 201

    # have to authenticate before calling DELETE
    @jwt_required()
    def delete(self):

        data = ModifyClient.parser.parse_args()
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM clients WHERE id=?"
        result = cursor.execute(query, (data['id'],))
        row = result.fetchone()

        if not row:
            return {'message': "A client with id '{}' was not found.".format(data['id'])}, 400

        query = "DELETE FROM clients WHERE id=?"
        cursor.execute(query, (data['id'],))
        connection.commit()
        connection.close()

        return {'message': 'Client has been successfully deleted!'}

    # have to authenticate before calling PUT
    @jwt_required()
    def put(self):

        data = ModifyClient.parser.parse_args()
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM clients WHERE id=?"
        result = cursor.execute(query, (data['id'],))
        row = result.fetchone()
        connection.close()

        client = {'id': data['id'], 'name': data['name'], 'email': data['email'], 'phone': data['phone'], \
                  'address': data['address'], 'city': data['city'], 'postalcode': data['postalcode'], \
                  'country': data['country']}

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        if row:
            query = "UPDATE clients SET name=?, email=?, phone=?, address=?, city=?, postalcode=?, country=? \
                     WHERE id=?"
            cursor.execute(query, (client['name'], client['email'], client['phone'], client['address'], \
                               client['city'], client['postalcode'], client['country'], client['id']))
        else:
            query = "INSERT INTO clients VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (client['id'], client['name'], client['email'], client['phone'], client['address'], \
                               client['city'], client['postalcode'], client['country']))
        connection.commit()
        connection.close()
        return client, 201


class ClientList(Resource):

    def get(self):
        result_list = []
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM clients"
        result = cursor.execute(query)

        for row in result:
            result_list.append({'client': {'id': row[0], 'name': row[1], 'email': row[2], 'phone number': row[3], \
            'address': row[4], 'city': row[5], 'postal code': row[6], 'country': row[7]}})

        connection.close()
        return result_list
