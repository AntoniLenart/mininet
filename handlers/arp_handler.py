
from ryu.lib.packet import packet, ethernet, arp

arp_table = {}


def arp_handler(datapath, eth, a, in_port) -> None:
    if a.src_ip not in arp_table:
        arp_table[a.src_ip] = eth.src
    print(arp_table)

    r = arp_table.get(a.dst_ip)
    if r:
        arp_resp = packet.Packet()
        arp_resp.add_protocol(ethernet.ethernet(ethertype=eth.ethertype,
                                                dst=eth.src, src=r))
        arp_resp.add_protocol(arp.arp(opcode=arp.ARP_REPLY,
                                      src_mac=r, src_ip=a.dst_ip,
                                      dst_mac=a.src_mac,
                                      dst_ip=a.src_ip))

        arp_resp.serialize()
        actions = [datapath.ofproto_parser.OFPActionOutput(in_port)]
        parser = datapath.ofproto_parser
        ofproto = datapath.ofproto
        out = parser.OFPPacketOut(datapath=datapath, buffer_id=ofproto.OFP_NO_BUFFER,
                                  in_port=ofproto.OFPP_CONTROLLER, actions=actions, data=arp_resp)
        datapath.send_msg(out)

        return
