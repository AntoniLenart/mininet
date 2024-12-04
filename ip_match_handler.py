from ryu.lib.packet import tcp, udp


def ip_match_handler(ip_pkt, parser):
    protocol = ip_pkt.proto

    # Default match
    match = parser.OFPMatch(
        eth_type=0x0800,
        ipv4_src=ip_pkt.src,
        ipv4_dst=ip_pkt.dst,
        ip_proto=protocol,
    )

    if protocol == 1:  # ICMP
        match = parser.OFPMatch(
            eth_type=0x0800,
            ipv4_src=ip_pkt.src,
            ipv4_dst=ip_pkt.dst,
            ip_proto=protocol,
        )

    elif protocol == 6:  # TCP
        tcp_pkt = ip_pkt.get_protocol(tcp.tcp)
        match = parser.OFPMatch(
            eth_type=0x0800,
            ipv4_src=ip_pkt.src,
            ipv4_dst=ip_pkt.dst,
            ip_proto=protocol,
            tcp_src=tcp_pkt.src_port,
            tcp_dst=tcp_pkt.dst_port,
        )

    elif protocol == 17:  # UDP
        udp_pkt = ip_pkt.get_protocol(udp.udp)
        match = parser.OFPMatch(
            eth_type=0x0800,
            ipv4_src=ip_pkt.src,
            ipv4_dst=ip_pkt.dst,
            ip_proto=protocol,
            udp_src=udp_pkt.src_port,
            udp_dst=udp_pkt.dst_port
        )

    return match
