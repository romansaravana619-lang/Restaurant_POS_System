# Local / LAN / Cloud Demo Deployment

![SaruPOS Local LAN Cloud Deployment](images/09_local_lan_cloud.png)

## Goal
Make StayEase and SaruPOS easy to demonstrate to clients.

## Levels
1. Localhost
2. LAN demo
3. Public/cloud demo

## SaruPOS current local ports
- Backend: `127.0.0.1:5000`
- Frontend: `localhost:5173`

## LAN demo
A client on the same network can access the host PC through its LAN IP and selected port after configuring the server to listen on the LAN interface. Windows Firewall may need to allow the selected port.

## StayEase next workflow
Open/clone project → identify entry point → create/use environment → install requirements → start → identify port → localhost test → LAN test → document exact client-demo command.

## Public demo
Remote clients require public deployment or a controlled tunnel. Production demos should use HTTPS and proper secret/configuration handling.

## Security
Never expose `.env`, JWT secrets, admin credentials or private production database data.
