//
//  NestedUser.swift
//
//
//  This file was auto-generated by Fern
//

import Foundation

public struct NestedUser: Codable {

    enum CodingKeys: String, CodingKey {
        case TEST = TEST
    }

    public let name: String
    public let nestedUser: User

}
