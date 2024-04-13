import math

import pygame

from settings import *


class Cube:
    def __init__(self, startSize, scale):
        self.points = []
        self.square = [
            Point(startSize, startSize, -startSize, scale, BLUE),
            Point(startSize, startSize, startSize, scale, RED),
            Point(startSize, -startSize, -startSize, scale, RED),
            Point(startSize, -startSize, startSize, scale, BLUE),
            Point(-startSize, startSize, -startSize, scale, RED),
            Point(-startSize, startSize, startSize, scale, BLUE),
            Point(-startSize, -startSize, -startSize, scale, BLUE),
            Point(-startSize, -startSize, startSize, scale, RED),
        ]
        self.triangle1 = [
            Point(startSize, startSize, startSize, scale, RED),
            Point(-startSize, -startSize, startSize, scale, RED),
            Point(-startSize, startSize, -startSize, scale, RED),
            Point(startSize, -startSize, -startSize, scale, RED),
        ]
        self.triangle2 = [
            Point(-startSize, startSize, startSize, scale, BLUE),
            Point(startSize, -startSize, startSize, scale, BLUE),
            Point(startSize, startSize, -startSize, scale, BLUE),
            Point(-startSize, -startSize, -startSize, scale, BLUE),
        ]
        self.octahedron = [
            Point(math.sqrt((startSize * startSize) * 2), 0, 0, scale, GREEN),
            Point(-math.sqrt((startSize * startSize) * 2), 0, 0, scale, GREEN),
            Point(0, math.sqrt((startSize * startSize) * 2), 0, scale, GREEN),
            Point(0, -math.sqrt((startSize * startSize) * 2), 0, scale, GREEN),
            Point(0, 0, math.sqrt((startSize * startSize) * 2), scale, GREEN),
            Point(0, 0, -math.sqrt((startSize * startSize) * 2), scale, GREEN),
        ]

        self.cone = self.makeCone(startSize, scale)
        self.dodecahedron = self.makeDodecahedron(startSize, scale)
        self.icosahedron = self.makeIcosahedron(startSize, scale)
        self.cylinder = self.makeCylinder(startSize, scale)
        self.circle = self.makeCircle(startSize, scale)
        self.torus = self.makeTorus(startSize, scale)

        self.startSize = startSize
        self.mode = 1
        self.pressed = False
        self.xOffset = 0
        self.yOffset = 0
        self.pivotPos = [0, 0, 0]
        self.camX = 0
        self.camY = 0
        self.camZ = 300
        self.xAngle = 0
        self.yAngle = 0
        self.zAngle = 0
        self.scale = 1
        self.moveSpeed = 5
        self.speed = 1

        self.setStart(self.mode, self.square)

    def setStart(self, mode, shape):
        self.points = shape
        self.pointLines = self.getLines(shape)
        if mode == 1:
            self.mode = 1
            self.scale = self.scale / self.camZ
        else:
            self.scale = self.scale

    def makeDodecahedron(self, startSize, scale):
        points = [
            Point(startSize, startSize, -startSize, scale, YELLOW),
            Point(startSize, startSize, startSize, scale, YELLOW),
            Point(startSize, -startSize, -startSize, scale, YELLOW),
            Point(startSize, -startSize, startSize, scale, YELLOW),
            Point(-startSize, startSize, -startSize, scale, YELLOW),
            Point(-startSize, startSize, startSize, scale, YELLOW),
            Point(-startSize, -startSize, -startSize, scale, YELLOW),
            Point(-startSize, -startSize, startSize, scale, YELLOW),
        ]
        gR = (1 + math.sqrt(5)) / 2
        print(gR)

        points.append(Point(startSize / gR, gR * startSize, 0, scale, GREEN))
        points.append(Point(startSize / gR, -gR * startSize, 0, scale, GREEN))
        points.append(Point(-startSize / gR, gR * startSize, 0, scale, GREEN))
        points.append(Point(-startSize / gR, -gR * startSize, 0, scale, GREEN))

        points.append(Point(gR * startSize, 0, startSize / gR, scale, BLUE))
        points.append(Point(-gR * startSize, 0, startSize / gR, scale, BLUE))
        points.append(Point(gR * startSize, 0, -startSize / gR, scale, BLUE))
        points.append(Point(-gR * startSize, 0, -startSize / gR, scale, BLUE))

        points.append(Point(0, startSize / gR, gR * startSize, scale, RED))
        points.append(Point(0, startSize / gR, -gR * startSize, scale, RED))
        points.append(Point(0, -startSize / gR, gR * startSize, scale, RED))
        points.append(Point(0, -startSize / gR, -gR * startSize, scale, RED))

        return points

    def makeIcosahedron(self, startSize, scale):
        gR = (1 + math.sqrt(5)) / 2
        points = []
        points.append(Point(0, startSize, startSize * gR, scale, BLUE))
        points.append(Point(0, startSize, -startSize * gR, scale, BLUE))
        points.append(Point(0, -startSize, startSize * gR, scale, BLUE))
        points.append(Point(0, -startSize, -startSize * gR, scale, BLUE))

        points.append(Point(startSize, startSize * gR, 0, scale, RED))
        points.append(Point(startSize, -startSize * gR, 0, scale, RED))
        points.append(Point(-startSize, startSize * gR, 0, scale, RED))
        points.append(Point(-startSize, -startSize * gR, 0, scale, RED))

        points.append(Point(startSize * gR, 0, startSize, scale, YELLOW))
        points.append(Point(-startSize * gR, 0, startSize, scale, YELLOW))
        points.append(Point(startSize * gR, 0, -startSize, scale, YELLOW))
        points.append(Point(-startSize * gR, 0, -startSize, scale, YELLOW))

        return points

    def makeCone(self, length, scale):
        points = []
        points.append(Point(0, length, 0, scale, YELLOW))
        for i in range(36):
            x = length * math.cos(math.radians(i * 10))
            z = length * math.sin(math.radians(i * 10))
            points.append(Point(x, -length, z, scale, YELLOW))
        return points

    def makeCylinder(self, length, scale):
        points = []
        for i in range(36):
            x = (length) * math.cos(math.radians(i * 10))
            z = (length) * math.sin(math.radians(i * 10))
            points.append(Point(x, length, z, scale, PURPLE))
            points.append(Point(x, -length, z, scale, PURPLE))
        return points

    def makeCircle(self, radius, scale):
        points = []
        radius = radius * 1.5
        for turnAng in range(18):
            for heightAng in range(18):
                tAng = math.radians(turnAng * 20)
                hAng = math.radians(heightAng * 20)
                x = radius * math.cos(tAng) * math.sin(hAng)
                y = radius * math.sin(tAng) * math.sin(hAng)
                z = radius * math.cos(hAng)
                points.append(Point(x, y, z, scale, ORANGE))

        return points

    def makeTorus(self, startSize, scale):
        points = []
        midRad = startSize * 1.5
        smallRad = startSize / 2
        for turnAng in range(18):
            for heightAng in range(18):
                tAng = math.radians(turnAng) * 20
                hAng = math.radians(heightAng) * 20

                x = (midRad + smallRad * math.cos(hAng)) * math.cos(tAng)
                y = smallRad * math.sin(hAng)
                z = (midRad + smallRad * math.cos(hAng)) * math.sin(tAng)
                points.append(Point(x, y, z, scale, RED))

        return points

    def movePoints(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.xOffset -= self.moveSpeed
        if keys[pygame.K_RIGHT]:
            self.xOffset += self.moveSpeed
        if keys[pygame.K_UP]:
            self.yOffset -= self.moveSpeed
        if keys[pygame.K_DOWN]:
            self.yOffset += self.moveSpeed
        if keys[pygame.K_MINUS]:
            self.scale /= 1.02
        if keys[pygame.K_EQUALS]:
            self.scale *= 1.02

        if keys[pygame.K_a]:
            self.speed += 0.05
        if keys[pygame.K_s]:
            self.speed -= 0.05

        # if keys[pygame.K_1]:
        #    self.zAngle += 1
        # if keys[pygame.K_2]:
        #    self.zAngle -= 1
        # if keys[pygame.K_3]:
        #    self.yAngle += 1
        # if keys[pygame.K_4]:
        #    self.yAngle -= 1
        # if keys[pygame.K_5]:
        #    self.xAngle += 1
        # if keys[pygame.K_6]:
        #    self.xAngle -= 1

        # if keys[pygame.K_f]:
        #    self.pivotPos[0] -= 1
        # if keys[pygame.K_h]:
        #    self.pivotPos[0] += 1
        # if keys[pygame.K_t]:
        #    self.pivotPos[1] -= 1
        # if keys[pygame.K_g]:
        #    self.pivotPos[1] += 1

        # if keys[pygame.K_j]:
        #    self.camX -= 4
        # if keys[pygame.K_l]:
        #    self.camX += 4
        # if keys[pygame.K_i]:
        #    self.camY -= 4
        # if keys[pygame.K_k]:
        #    self.camY += 4
        # if keys[pygame.K_u]:
        #    self.camZ -= 4
        # if keys[pygame.K_o]:
        #    self.camZ += 4

        if keys[pygame.K_1]:
            self.points = self.square
            self.pointLines = self.getLines(self.points)
        if keys[pygame.K_2]:
            self.points = self.triangle1
            self.pointLines = self.getLines(self.points)
        if keys[pygame.K_3]:
            self.points = self.triangle2
            self.pointLines = self.getLines(self.points)
        if keys[pygame.K_4]:
            self.points = self.octahedron
            self.pointLines = self.getLines(self.points)
        if keys[pygame.K_5]:
            self.points = self.cone
            self.pointLines = self.getLines(self.points)
        if keys[pygame.K_6]:
            self.points = self.cylinder
            self.pointLines = self.getLines(self.points)
        if keys[pygame.K_7]:
            self.points = self.circle
            self.pointLines = self.getLines(self.points)
        if keys[pygame.K_8]:
            self.points = self.torus
            self.pointLines = self.getLines(self.points)
        if keys[pygame.K_9]:
            self.points = self.dodecahedron
            self.pointLines = self.getLines(self.points)
        if keys[pygame.K_0]:
            self.points = self.icosahedron
            self.pointLines = self.getLines(self.points)

        if keys[pygame.K_SPACE] and not self.pressed:
            self.pressed = True
            if self.mode == 0:
                self.mode = 1
                self.scale = self.scale / self.camZ

            elif self.mode == 1:
                self.mode = 0
                self.scale = self.scale * self.camZ

        if keys[pygame.K_SPACE] == False and self.pressed:
            self.pressed = False

    def update(self):
        self.movePoints()
        self.xAngle += self.speed
        self.yAngle += self.speed
        self.zAngle += 0

    def getLines(self, shape):
        connections = []
        if shape == self.cone:
            point1 = self.cone[0]
            for i in range(1, len(self.points)):
                point2 = self.cone[i]
                connections.append((point1, point2))

        for i in range(len(self.points) - 1):
            for j in range(i + 1, len(self.points)):
                point1 = self.points[i]
                point2 = self.points[j]

                if shape == self.square and (
                    (point1.z == point2.z and point1.y == point2.y)
                    or (point1.z == point2.z and point1.x == point2.x)
                    or (point1.x == point2.x and point1.y == point2.y)
                    or (point1.x == point2.x and point1.z == point2.z)
                    or (point1.y == point2.y and point1.x == point2.x)
                    or (point1.y == point2.y and point1.z == point2.z)
                ):
                    connections.append((point1, point2))

                if shape == self.triangle1 or shape == self.triangle2:
                    connections.append((point1, point2))
                if shape == self.octahedron and not (
                    (point1.x != 0 and point2.x != 0)
                    or (point1.y != 0 and point2.y != 0)
                    or (point1.z != 0 and point2.z != 0)
                ):
                    connections.append((point1, point2))

                if shape == self.dodecahedron:
                    if self.dodecahedronLines(self.startSize, point1, point2):
                        connections.append((point1, point2))

                if shape == self.cylinder and (
                    (point1.x == point2.x and point1.z == point2.z)
                ):
                    connections.append((point1, point2))

                if shape == self.circle:
                    if self.circleLines(self.startSize, point1, point2):
                        connections.append((point1, point2))
                if shape == self.torus:
                    if self.torusLines(self.startSize, point1, point2):
                        connections.append((point1, point2))
                if shape == self.icosahedron:
                    if self.icosahedronLines(self.startSize, point1, point2):
                        connections.append((point1, point2))

        return connections

    def dodecahedronLines(self, startSize, point1, point2):
        distance = math.sqrt(
            math.pow(point2.x - point1.x, 2)
            + math.pow(point2.y - point1.y, 2)
            + math.pow(point2.z - point1.z, 2)
        )

        edgeLength = (math.sqrt(5) * startSize) - startSize

        if edgeLength == distance:
            return True

        return False

    def icosahedronLines(self, startSize, point1, point2):
        distance = math.sqrt(
            math.pow(point2.x - point1.x, 2)
            + math.pow(point2.y - point1.y, 2)
            + math.pow(point2.z - point1.z, 2)
        )

        edgeLength = startSize * 2

        if edgeLength == distance:
            return True

        return False

    def circleLines(self, startSize, point1, point2):
        distance = math.sqrt(
            math.pow(point2.x - point1.x, 2)
            + math.pow(point2.y - point1.y, 2)
            + math.pow(point2.z - point1.z, 2)
        )
        if distance < startSize / 1.5:
            return True
        return False

    def torusLines(self, startSize, point1, point2):
        distance = math.sqrt(
            math.pow(point2.x - point1.x, 2)
            + math.pow(point2.y - point1.y, 2)
            + math.pow(point2.z - point1.z, 2)
        )
        if startSize / 3 < distance < startSize / 1.2 and point1.y == point2.y:
            return True
        return False

    def displayLines(self, screen):
        for connection in self.pointLines:
            point1Pos = connection[0].pos
            point2Pos = connection[1].pos
            aveSize = (connection[0].scale + connection[1].scale) // 4
            pygame.draw.line(
                screen,
                WHITE,
                (point1Pos[0], point1Pos[1]),
                (point2Pos[0], point2Pos[1]),
                int(aveSize),
            )

    def displayCube(self, screen):
        self.displayLines(screen)
        for point in self.points:
            point.displayPoint(
                screen,
                self.xOffset,
                self.yOffset,
                self.scale,
                self.pivotPos,
                self.xAngle,
                self.yAngle,
                self.zAngle,
                self.camX,
                self.camY,
                self.camZ,
                self.mode,
            )
        # if self.mode == 0:
        #    pygame.draw.circle(
        #        screen,
        #        RED,
        #        (
        #            (self.pivotPos[0] / self.scale) + self.xOffset,
        #            (self.pivotPos[1] / self.scale) + self.yOffset,
        #        ),
        #        10,
        #    )
        # else:
        #    pX = (
        #        (self.pivotPos[0] + self.camX)
        #        / (self.pivotPos[2] + self.camZ)
        #        / self.scale
        #        + self.xOffset
        #        + WIDTH // 2
        #    )
        #    pY = (
        #        (self.pivotPos[1] + self.camY)
        #        / (self.pivotPos[2] + self.camZ)
        #        / self.scale
        #        + self.yOffset
        #        + HEIGHT // 2
        #    )
        #    pygame.draw.circle(screen, RED, (pX, pY), 10 / self.camZ / self.scale)


class Point:
    def __init__(self, x, y, z, size, color):
        self.x = x
        self.y = y
        self.z = z
        self.size = size
        self.scale = size
        self.color = color
        self.pos = [x, y]

    def displayPoint(
        self,
        screen,
        xOffset,
        yOffset,
        scale,
        pivotPos,
        xAngle,
        yAngle,
        zAngle,
        camX,
        camY,
        camZ,
        mode,
    ):

        if scale != 0:
            xR = self.x - pivotPos[0]
            yR = self.y - pivotPos[1]
            zR = self.z - pivotPos[2]

            ZX = (
                xR * math.cos(math.radians(zAngle))
                - yR * math.sin(math.radians(zAngle))
                - xR
            )
            ZY = (
                xR * math.sin(math.radians(zAngle))
                + yR * math.cos(math.radians(zAngle))
                - yR
            )
            YX = (
                (xR + ZX) * math.cos(math.radians(yAngle))
                - zR * math.sin(math.radians(yAngle))
                - (xR + ZX)
            )
            YZ = (
                (xR + ZX) * math.sin(math.radians(yAngle))
                + zR * math.cos(math.radians(yAngle))
                - zR
            )
            XY = (
                (yR + ZY) * math.cos(math.radians(xAngle))
                - (zR + YZ) * math.sin(math.radians(xAngle))
                - (yR + ZY)
            )
            XZ = (
                (yR + ZY) * math.sin(math.radians(xAngle))
                + (zR + YZ) * math.cos(math.radians(xAngle))
                - (zR + YZ)
            )

            xRotationOffset = YX + ZX
            yRotationOffset = XY + ZY
            zRotationOffset = XZ + YZ

            if mode == 0:
                x = (self.x + xRotationOffset + camX) / scale + xOffset + WIDTH // 2
                y = (self.y + yRotationOffset + camY) / scale + yOffset + HEIGHT // 2
                self.scale = self.size / scale
            else:
                z = self.z + zRotationOffset + camZ
                x = (self.x + xRotationOffset + camX) / z / scale + xOffset + WIDTH // 2
                y = (
                    (self.y + yRotationOffset + camY) / z / scale
                    + yOffset
                    + HEIGHT // 2
                )
                self.scale = self.size / z / scale

            self.pos = [x, y]
            if mode == 0:
                pygame.draw.circle(screen, self.color, (x, y), self.size / scale)
            else:
                pygame.draw.circle(screen, self.color, (x, y), self.size / z / scale)
