import { Flex, FlexProps, VStack, Text, Link } from "@chakra-ui/react";
interface FooterProps extends FlexProps {}
const Footer: React.FC<FooterProps> = (props) => {
  return (
    <VStack
      bg="gLightGray"
      p={3}
      borderTop="3px solid"
      borderTopColor="gGray"
    >
      <Text color="gBlack">
        문의 :{" "}
        <Link href="mailto:siyea0405@gmail.com" isExternal>
          siyea0405@gmail.com
        </Link>
      </Text>
      <Flex direction="column" w="100%" bg="gLightGray">
        <Text
          fontSize="xs"
          color="gDarkGray"
          borderTop="1px solid"
          borderTopColor="gGray"
        >
          OliveDB는 개인이 만든 취미 프로젝트이며 Oliveyoung과 제휴하지
          않습니다.
        </Text>
        <Text fontSize="xs" color="gDarkGray">
          주기적인 업데이트 후 제품 가격이 변경되므로, OliveYoung의 제품
          가격과 다르게 조회될 수 있습니다.
        </Text>
      </Flex>
    </VStack>
  );
};
export default Footer;
