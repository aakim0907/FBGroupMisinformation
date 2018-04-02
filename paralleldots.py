import paralleldots

api_key   = "4FJEnSvGxUI6FCYl64yWK2iDE4AqZpQso150wqrilr0"
text      = "Prime Minister Narendra Modi tweeted a link to the speech Human Resource Development Minister Smriti Irani made in the Lok Sabha during the debate on the ongoing JNU row and the suicide of Dalit scholar Rohith Vemula at the Hyderabad Central University."

paralleldots.set_api_key(api_key)

print( paralleldots.keywords( text ) )
